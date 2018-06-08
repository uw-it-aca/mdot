FROM python:2.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt
RUN django-admin.py startproject project .
ADD docker /app/project/
