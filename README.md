

# collaborative-planning-app

Prototype app for collaborative assessment of task complexity


### Requirements
- Docker
- Docker Compose


### Technologies used

#### OS/Containerization:
	- Docker
	- Alpine

#### Datastore:
	- MySQL

#### Backend:
	- Python
	- Flask
	- Flask-SocketIO
	- mysqlclient

#### Web Client:
	- Vue.js
	- Socket.IO


---


### Setup for Running the Application Locally

clone the repo and go to directory
```sh
git clone https://github.com/hsadler/collaborative-planning-app
cd collaborative-planning-app
```

build the app base image
```sh
docker build \
	--no-cache \
	-f=base.Dockerfile \
	-t=collaborative-planning-app-base:v1 .
```

spin-up services with docker compose
```sh
docker-compose -f docker-compose.yaml up --build --force-recreate \
	--remove-orphans --abort-on-container-exit
```

#### in a separate terminal...

create the necessary mysql tables
```sh
docker exec -it collaborative-planning-app \
	bash -c "cd server/scripts/ && python create_tables.py"
```

populate the `vote_variant` table
```sh
docker exec -it collaborative-planning-app \
	bash -c "cd server/scripts/ && python populate_vote_variant_table.py"
```

navigate to application in browser
```sh
http://localhost/
```


---


### Dev Commands

spin-up services with docker compose
```sh
docker-compose -f docker-compose-dev.yaml up --build --force-recreate \
	--remove-orphans --abort-on-container-exit
```

#### in a separate terminal...

start the npm build watcher
```sh
docker exec -it collaborative-planning-app \
	bash -c "cd client/ && npm run build-dev"
```

connect to python-flask server container
```sh
docker exec -it collaborative-planning-app bash
```

connect to mysql container, start mysql cli, and select database
```sh
docker exec -it collaborative-planning-app-mysql \
	mysql --user=root --password=password collaborative-planning-app
```

create some mock data
```sh
docker exec -it collaborative-planning-app \
	bash -c "cd server/scripts/ && python populate_mock_data.py"
```

test api with shell script
```sh
source tests/test_api.sh
```


