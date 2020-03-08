

# collaborative-planning-app

Prototype app for collaborative assessment of task complexity


## Requirements
- Docker
- Python3


---


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
```


---


### Dev notes

install python requirements
```sh
pip install -r requirements.txt
```

spin-up dev server
```sh
python server/main.py
```

build image for testing
```sh
docker build \
	--no-cache \
	-f=Dockerfile \
	-t=collaborative-planning-app:local .
```

run image for testing
```sh
docker run -it --rm -p 80:80 \
	--name collaborative-planning-app collaborative-planning-app:local
```




