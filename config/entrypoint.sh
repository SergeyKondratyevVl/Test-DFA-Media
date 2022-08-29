#! /bin/bash

echo started
# apt update
python manage.py makemigrations gallery --no-input
python manage.py migrate --no-input
exec gunicorn openapi.wsgi:application -b 0.0.0.0:8000 --reload

