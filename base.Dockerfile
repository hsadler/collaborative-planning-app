
# parent image
FROM python:3.6-alpine

# OS installs
RUN apk add --no-cache \
	nodejs \
	nodejs-npm \
	bash \
	mariadb-dev \
	build-base
