#generic python2.7 image
FROM python:2.7
ENV PYTHONUNBUFFERED 1

#python3.x & node8.x
#FROM nikolaik/python-nodejs:latest

#python2.7.12 & node6.9.2
#FROM beevelop/nodejs-python:latest

# copy contents of repo into an 'app' directory on container
ADD . /app/
WORKDIR /app

# install python dependency packages (via setup.py) on container
RUN pip install -r requirements.txt
COPY docker/manage.py /app/manage.py
