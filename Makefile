su:
	docker compose run --rm web-app sh -c "python manage.py createsuperuser"
	echo 'LLLLLLLLLLL'
	@echo 'DDDDDDDDDDDDDD'


newapp:
	docker compose run --rm web-app sh -c "python manage.py startapp $(app)"

from_file:
	@sh from_file.sh
