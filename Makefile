
dev:
	docker-compose -f docker-compose-dev.yaml up --build --force-recreate \
	--remove-orphans --abort-on-container-exit

dev-watch:
	docker exec -it collaborative-planning-app \
	bash -c "cd client/ && npm run build-dev"