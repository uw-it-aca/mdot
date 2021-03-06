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



### Running the app against a live rest API ###

In your `.env` file, uncomment these two lines or add them if they are not there:

    $ RESTCLIENTS_MDOT_DAO_CLASS=Live
    $ RESTCLIENTS_MDOT_HOST=http://localhost:8000/

This will run mdot against a live API. Make sure mdot-rest is running on a different port and set `RESTCLIENTS_MDOT_HOST` accordingly. If you would like to go back to Mock mode, set the following:

    $ RESTCLIENTS_MDOT_DAO_CLASS=Mock


### Running unit tests inside the Docker container ###
To run the unit tests, simply run the following command from the repository root:

    $ docker-compose run --rm app bash -c ". bin/activate && python manage.py test"
