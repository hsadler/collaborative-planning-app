
FROM collaborative-planning-app-base:v1

# python installs
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# # npm installs
# COPY app/client/package.json /tmp/package.json
# RUN cd /tmp && \
# 	npm install && \
# 	mkdir -p /app/client && \
# 	cp -a /tmp/node_modules /app/client/

# copy app
COPY ./app /app
WORKDIR /app

# # npm build
# RUN cd /app/client && \
	# npm run build

# the rest is handled by the docker-compose.yaml file
