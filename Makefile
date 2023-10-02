su:
	docker compose run --rm web-app sh -c "python manage.py createsuperuser"
	echo 'LLLLLLLLLLL'
	@echo 'DDDDDDDDDDDDDD'


newapp:
	docker compose run --rm web-app sh -c "python manage.py startapp $(app)"

migrations:
	docker compose run --rm web-app sh -c "python manage.py makemigrations"

migrate:
	docker compose run --rm web-app sh -c "python manage.py migrate"

from_file:
	@sh from_file.sh
