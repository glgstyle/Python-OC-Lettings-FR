# base image
FROM python:3.11.5-alpine

# setup environment variable
ENV DockerHOME=/app

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
# prevent python from creating byte files
ENV PYTHONDONTWRITEBYTECODE 1
# don't use buffer memory to store language data (make it faster)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME
# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the Django app runs
EXPOSE 8000:8000
# start server 

CMD ["gunicorn", "--bind", " 0.0.0.0:8000", "--workers", "3", "oc_lettings_site.wsgi:application"]