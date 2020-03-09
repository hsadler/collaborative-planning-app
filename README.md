

# collaborative-planning-app

Prototype app for collaborative assessment of task complexity


### Requirements
- Docker
- Docker Compose
<!-- - Python3 -->


<!-- ---


### All Following Commands Expect a Python Virtual Environment

create virtual environment directory for python
```sh
python3 -m venv venv
```
start virtualenv
```sh
source venv/bin/activate
```
deactivate the virtual environment when finished
```sh
deactivate
``` -->


---


### Setup

spin-up services with docker compose
```sh
docker-compose -f docker-compose.yaml up --build --force-recreate \
	--remove-orphans --abort-on-container-exit
```

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


### Dev Commands (requires local containers to be running via docker-compose)

connect to python-flask server container
```sh
docker exec -it collaborative-planning-app bash
```

connect to mysql container, start mysql cli, and select database
```sh
docker exec -it collaborative-planning-app-mysql \
	mysql --user=root --password=password collaborative-planning-app
```

test api with curl
```sh
# user api
curl http://localhost/api/create-user?user_name=jimmy
curl http://localhost/api/get-all-users
# task api
curl http://localhost/api/create-task?task_title=mytask
curl http://localhost/api/get-all-tasks-simple-metadata
curl http://localhost/api/get-task-by-id?task_id=taskid
# vote api
curl http://localhost/api/create-or-update-vote?user_id=userid&task_id=taskid&vote_variant=5
curl http://localhost/api/get-all-votes-by-task?task_id=taskid
# vote_variant api
curl http://localhost/api/get-available-vote-variants
```


