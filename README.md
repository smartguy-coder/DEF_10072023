pip install djangorestframework
pip install psycopg2-binary
docker compose run --rm web-app sh -c "django-admin startproject library ."
docker compose run --rm web-app sh -c "python manage.py createsuperuser"