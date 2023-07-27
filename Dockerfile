# base image
FROM python:3.8

# create and set working directory
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

# copy project to the docker image
COPY . /app
# port where the Django app runs
EXPOSE 8000
# start server
CMD python manage.py runserver 0.0.0.0:8000