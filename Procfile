web: gunicorn Breachxpress.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py createsuperuser --noinput --username admin --email admin@example.com --password yourpassword123

