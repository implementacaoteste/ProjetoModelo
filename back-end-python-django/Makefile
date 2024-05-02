#Makefile

IMAGE_NAME = image_python_django
CONTAINER_NAME = container_python_django

# Tarefa para construir a imagem Docker da aplicação
build:
	docker-compose build --build-arg IMAGE_NAME=$(IMAGE_NAME)

# Tarefa para iniciar os serviços Docker (aplicação e banco de dados)
up:
	docker-compose up -d

# Tarefa para parar e remover os serviços Docker
down:
	docker-compose down

# Tarefa para executar o servidor Django localmente
run:
	python manage.py runserver

# Tarefa para criar e aplicar migrações no banco de dados
migrate:
	python manage.py makemigrations
	python manage.py migrate

# Tarefa para executar os testes da aplicação
test:
	python manage.py test

# Tarefa para exibir os logs dos serviços Docker
logs:
	docker-compose logs

# Tarefa para acessar o terminal interativo do contêiner da aplicação
interativo:
	docker-compose up -d
	docker-compose exec app bash

ps:
	docker ps -a