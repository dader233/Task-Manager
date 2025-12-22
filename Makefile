migrate:
	docker-compose run --rm django python manage.py migrate

run:
	docker-compose up

shell:
	docker-compose run --rm django python manage.py shell

test:
	docker-compose run --rm django python manage.py test

make migrate
make run