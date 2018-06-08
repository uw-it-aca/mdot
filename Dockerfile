#generic python2.7 image
#FROM python:2.7

#python3.x & node8.x
#FROM nikolaik/python-nodejs:latest

#python2.7.12 & node6.9.2
FROM beevelop/nodejs-python:latest

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt
RUN django-admin.py startproject project .
ADD docker /app/project/
