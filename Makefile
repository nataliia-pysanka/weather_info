#cnf ?= .env
#include $(cnf)
#export $(shell sed 's/=.*//' $(cnf))
up:
	sudo docker-compose up --build
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps
stop:
	sudo docker-compose down
clear:
	sudo docker system prune -a
