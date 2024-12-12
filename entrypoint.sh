#!/bin/bash

# Apply database migrations
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input --clear

# Create superuser if it doesn't exist
python manage.py shell <<EOF
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Set superuser credentials, either from environment variables or hardcoded
superuser_username = 'admin'
superuser_email = 'admin@example.com'
superuser_password = '1234'  # You can replace this with an env variable for security

try:
    User.objects.get(username=superuser_username)
except ObjectDoesNotExist:
    User.objects.create_superuser(superuser_username, superuser_email, superuser_password)
EOF

# Start server
python manage.py runserver 0.0.0.0:10000
