# ./django-ninja/Makefile

IMAGE_NAME = image_python_django
CONTAINER_BACKEND = container_backend

.PHONY: venv build up down run migrate test logs backend ps mysql restart clear

# Tarefa para criar o ambiente virtual
venv:
	apt-get update && \
	apt-get install -y build-essential libmariadb-dev-compat && \
	python3 -m venv env && \
	source env/bin/activate && \
	pip install -r requirements.txt

# Tarefa para construir a imagem Docker da aplicação
build:
	mkdir -p db_mysql
	docker-compose build

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
	docker exec $(CONTAINER_BACKEND) python manage.py makemigrations --no-input && \
	docker exec $(CONTAINER_BACKEND) python manage.py migrate --no-input

# Tarefa para executar os testes da aplicação
test:
	python manage.py test

# Tarefa para exibir os logs dos serviços Docker
logs:
	docker-compose logs

# Tarefa para acessar o terminal interativo do contêiner da aplicação
backend:
	docker-compose exec backend bash

# Tarefa para exibir os contêineres e imagens Docker
ps:
	docker ps -a && \
	docker images

# Tarefa para acessar o MySQL do contêiner
mysql:
	docker exec -it container_db mysql -u $(DB_USER) -p

# Tarefa para reiniciar os serviços Docker
restart: down build up ps

# Tarefa para limpar o ambiente de desenvolvimento
clear:
	make down
	docker rmi django-ninja-backend mysql -f
	docker image prune -f
	rm -rf db_mysql
	python3 scripts/remove_pycache.py
	docker ps
	docker images
	sleep 2
	clear


