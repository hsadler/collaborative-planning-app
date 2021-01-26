
# fresh setup

setup: build-base build-app

setup-db:
	docker-compose exec webapp bash -c "cd server/scripts/ && \
	python create_tables.py && python populate_vote_variant_table.py"


# development

up:
	docker-compose -f docker-compose-dev.yaml up -d && make fe-watch

down:
	docker-compose -f docker-compose-dev.yaml down

be-logs:
	docker-compose -f docker-compose-dev.yaml logs -f webapp

db-logs:
	docker-compose -f docker-compose-dev.yaml logs -f mysql

be-shell:
	docker-compose -f docker-compose-dev.yaml exec webapp bash

db-shell:
	docker-compose -f docker-compose-dev.yaml exec mysql \
	mysql --user=root --password=password collaborative-planning-app


# component commands
build-base:
	docker build \
	--no-cache \
	-f=base.Dockerfile \
	-t=collaborative-planning-app-base:v1 .

build-app:
	docker-compose -f docker-compose-dev.yaml build

fe-watch:
	docker-compose -f docker-compose-dev.yaml exec webapp \
	bash -c "cd client/ && npm run build-dev"
