# ./django-ninja/Makefile

IMAGE_NAME = image_python_django
CONTAINER_BACKEND = container_backend

PYTHON = python3
VENV_NAME = env
VENV_DIR = $(CURDIR)/$(VENV_NAME)
PIP = $(VENV_DIR)/bin/pip
ACTIVATE = $(VENV_DIR)/bin/activate

# Tarefa para criar o ambiente virtual
venv:
	apt-get update
	apt-get install -y build-essential libmysqlclient-dev
	$(PYTHON) -m venv $(VENV_NAME)
	source $(ACTIVATE)
	$(PIP) install -r requirements.txt

# Tarefa para construir a imagem Docker da aplicação
build:
	mkdir -p db_mysql
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

sleep:
	sleep 20

# Tarefa para criar e aplicar migrações no banco de dados
migrate_sleep: sleep migrate

migrate:
	docker exec $(CONTAINER_BACKEND) python manage.py makemigrations --no-input
	docker exec $(CONTAINER_BACKEND) python manage.py migrate --no-input
	# docker exec $(CONTAINER_BACKEND) python manage.py seeds_produto
	# @echo "Seeds da entidade Produto criados com sucesso!"

# Tarefa para executar os testes da aplicação
test:
	python manage.py test

# Tarefa para exibir os logs dos serviços Docker
logs:
	docker-compose logs

# Tarefa para acessar o terminal interativo do contêiner da aplicação
backend:
	docker-compose exec backend bash

ps:
	docker ps -a
	docker images

mysql:
	docker exec -it container_db mysql -u usuario_db -p

restart: down build up ps

make_app:
    # make criar APP_NOME=meu_app
	python3 scripts/criar_app.py $(APP_NOME)
	
make_entity:
	# make criar_entidade APP_NOME=aplicativo ENTIDADE_NOME=fornecedor
	python3 scripts/criar_entidade.py $(APP_NOME) $(ENTIDADE_NOME)

clear:
	clear
	make down
	docker rmi django-ninja-backend
	docker rmi mysql
	docker image prune
	rm -rf db_mysql
	python3 scripts/remove_pycache.py
	docker ps
	docker images
	sleep 2
	clear

