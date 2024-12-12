#!/bin/bash

# Apply database migrations
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input --clear

# Start server
python manage.py runserver 0.0.0.0:10000
