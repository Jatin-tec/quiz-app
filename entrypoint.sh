# Apply database migrations
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input --clear

# Create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '1234')" | python manage.py shell

# Start server
python manage.py runserver 0.0.0.0:10000
