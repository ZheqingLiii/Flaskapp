# Flaskapp

This is a practice project using Nginx as HTTP webserver and uWSGI as application server deploying a Flask app on a virtual machine

# Structure
app
├── docker-compose.yml
├── flask
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── app
│   │   ├── __init__.py
│   │   └── views.py
│   ├── app.ini
│   ├── requirements.txt
│   └── run.py
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── .gitignore

