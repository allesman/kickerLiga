# base image
FROM python:3.8
# setup environment variable
# ENV DockerHOME=/home/app/webapp

# set work directory
# RUN mkdir -p $DockerHOME

# where your code lives
# WORKDIR $DockerHOME
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements to the docker image
COPY requirements.txt /app
# install dependencies
RUN pip install --upgrade pip
# run this command to install all dependencies
RUN pip install -r requirements.txt

# copy whole project to your docker home directory.
# COPY . $DockerHOME
COPY . /app
# port where the Django app runs
EXPOSE 8000
# start server
CMD python manage.py runserver 0.0.0.0:8000