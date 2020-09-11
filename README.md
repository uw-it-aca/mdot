# MDOT APP #

This README documents whatever steps are necessary to get your application up and running.

## Installation ##

### Prerequisites ###
To run the app, you must have the following installed:
* Docker
* Docker-compose

### Steps to run ###
First, clone the app:

    $ git clone https://github.com/uw-it-aca/mdot.git

Navigate to the develop branch and copy the sample environment variables into your own `.env` file:

    $ cd mdot
    $ git checkout develop
    $ cp sample.env .env

Then, run the following command to build your docker container:

    $ docker-compose up --build

You should see the server running when viewing http://localhost:8000 (or at the port set in your `.env` file)

## Development ##

### Running the app with Docker ###

To rebuild the docker container from scratch, run: 

    $ docker-compose up --build

Otherwise, just run:

    $ docker-compose up

### Running unit tests inside the Docker container ###
First, make sure that your docker container is up and running. Then, in a separate terminal, run the following command to get the __CONTAINER  ID__ of the current build:

    $ docker ps

Then, to start an interactive terminal, run the following command, replacing {CONTIANER_ID} with the container ID of the running docker container:

    $ docker exec -it {CONTAINER_ID} /bin/bash

Now you are in the container! To run the unit tests, activate the virtual env and run the test command:

    $ . bin/activate
    $ python manage.py test
