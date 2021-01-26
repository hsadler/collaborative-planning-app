

# collaborative-planning-app

Prototype app for collaborative assessment of task complexity


### Requirements
- Docker
- Docker Compose


---


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


### Initial Setup for Running the Application Locally

1. run `make setup` to build the "base" and "app" images
2. run `make up` to spin-up the webapp and mysql containers
3. in a separate terminal, run `make setup-db` to create and populate the MySQL tables
4. navigate to application in browser `http://localhost/`
5. `ctl-c` the original terminal and run `make down` to spin-down the containers


---


### Development Commands

`make up`: spin-up containers which serve the web app to `http://localhost/`

`make down`: spin-down containers

Other dev commands are available in the Makefile.

