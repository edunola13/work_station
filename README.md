# Work Station

## Notes
When compiling pyzmq (e.g. installing with pip on Linux), it is generally recommended that zeromq be installed separately, via homebrew, apt, yum, etc:
 - sudo apt-get install libzmq3-dev (For Linux)

## Dependencies
Only run in Linux
 - Python 3
 - sudo apt-get install libzmq3-dev
 - Redis

## Initial Steps
 - Clone repo
 - Create and activate virtual env
 - Install requeriment (pip)

## Environment Variables
Create .env variables and/or set the environme+nt variables.
Use like example .env.example
https://pypi.org/project/python-dotenv/

## Redis
https://redis.io/download
Conviene usar un docker

## Celery
https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7
"""
For dev: celery -A src.modules.celery worker -l info -B
"""

"""
For prod: 
celery -A src.modules.celery worker -l info
celery -A src.modules.celery beat -l info
"""

## Dockers

### Build
Dockerfiles are located in dockers. We have one Dockerfile for all the entrypoints.
In the entrypoint are defined all the posibilities.

sudo docker build -t work_station . -f dockers/Dockerfile

### Run
sudo docker run --env-file .env work_station {action}

add "-d" to run in background

### Docker Compose
Move to /dockers folder and run
docker-compose pull && docker-compose up

### Docker Monitor
sudo docker stats ===>>> Monitorea los contenedores corriendo
sudo docker exec -it ID_CONTAINER bash ===>>> Entrar al container
sudo docker exec -it 564600ef2b7b /bin/sh ===>>> Entrar al container
ifconfig ===>>> Info de Red
docker logs ID_CONTAINER ===>>> Ver log
