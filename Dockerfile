#generic python2.7 image
FROM python:2.7
ENV PYTHONUNBUFFERED 1

# copy contents of repo into an 'app' directory on container
ADD . /app/
WORKDIR /app

# install python dependency packages (via setup.py) on container
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY sampleproj/manage.py /app/manage.py
