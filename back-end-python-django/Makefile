# Tarefa para construir a imagem Docker da aplicação
build:
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
	python manage.py makemigrations
	python manage.py migrate

# Tarefa para executar os testes da aplicação
test:
	python manage.py test