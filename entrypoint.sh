#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate

daphne basic.asgi:application --port 8000 --bind 0.0.0.0