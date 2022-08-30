#! /bin/bash

echo started
# apt update
python manage.py makemigrations gallery --no-input
python manage.py migrate --no-input
python manage.py test --no-input
exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload
