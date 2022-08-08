#! /bin/bash

python manage.py makemigrations
python manage.py migrate
sudo uwsgi --ini uwsgi.ini
