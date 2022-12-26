
up:
	sudo docker-compose up --build
migrate:
	python3 manage.py migrate
user:
	python3 manage.py createsuperuser
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps
stop:
	sudo docker-compose down
clear:
	sudo docker system prune -a
