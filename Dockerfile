#generic python3.6 image
# maybe use version 1.1.0
FROM acait/django-container:1.0.38 as app-container

USER root
# install system and python dependency packages (via setup.py) on container
RUN apt-get update -y && apt-get install -y libxmlsec1 libxmlsec1-dev
USER acait

ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/
ADD --chown=acait:acait README.md /app/

RUN . /app/bin/activate && pip install -r requirements.txt

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker project


