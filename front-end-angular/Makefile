# ./front-end-angular/Makefile

# Obter o nome da pasta atual
DIR_NAME := $(shell basename "$(PWD)")

# Variável para o nome do serviço no docker-compose
SERVICE_NAME = frontend
TAG = latest

build:
	ng build
	docker-compose build $(SERVICE_NAME)

run:
	docker run -p 8080:80 $(SERVICE_NAME):$(TAG)

clear:
	make down
	docker rmi -f $(DIR_NAME)-$(SERVICE_NAME):$(TAG)
	docker image prune	
	docker ps -a
	docker images
	
up:
	docker-compose up -d $(SERVICE_NAME)

down:
	docker-compose down

ps:
	docker ps -a
	docker images

app:
	docker-compose exec app sh


restart: down build up ps

