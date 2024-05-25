#!/bin/bash

cd /code/

pip3 install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate auth
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:9001 --insecure

