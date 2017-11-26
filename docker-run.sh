#!/usr/bin/env bash

cd /home/application/app
ldconfig
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
cd /home/application
