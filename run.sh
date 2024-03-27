python manage.py collectstatic --noinput
python manage.py migrate
gunicorn attachment_download.wsgi --bind=0.0.0.0:80