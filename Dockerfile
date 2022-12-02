ARG DJANGO_CONTAINER_VERSION=1.4.1

FROM gcr.io/uwit-mci-axdd/django-container:${DJANGO_CONTAINER_VERSION} as app-prebundler-container

USER root

RUN apt-get update && apt-get install libpq-dev -y
RUN apt-get update && apt-get install mysql-client libmysqlclient-dev -y

USER acait

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ /app/project/

RUN /app/bin/pip install -r requirements.txt
RUN /app/bin/pip install  mysqlclient

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ project/
ADD --chown=acait:acait docker/app_deploy.sh /scripts
ADD --chown=acait:acait docker/app_start.sh /scripts
RUN chmod u+x /scripts/app_deploy.sh

FROM node:14.18.1-stretch AS node-bundler

ADD ./package.json /app/
WORKDIR /app/
RUN npm install .

ADD . /app/

ARG VUE_DEVTOOLS
ENV VUE_DEVTOOLS=$VUE_DEVTOOLS
RUN npm run build

FROM app-prebundler-container as app-container

# ADD --chown=acait:acait . /app/
# ADD --chown=acait:acait docker/ project/

COPY --chown=acait:acait --from=node-bundler /app/mdot/static /app/mdot/static

RUN /app/bin/python manage.py collectstatic --noinput

FROM gcr.io/uwit-mci-axdd/django-test-container:${DJANGO_CONTAINER_VERSION} as app-test-container

ENV NODE_PATH=/app/lib/node_modules
COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
