# ./Makefile

# Nome dos containers
CONTAINER_BACKEND = container_backend
CONTAINER_FRONTEND = container_frontend
CONTAINER_DB = container_db

# Caminhos dos subdiretórios
DIR_BACKEND = ./django-ninja
DIR_FRONTEND = ./front-end-angular

# Tarefa para construir as imagens Docker
build:
	docker-compose build

# Tarefa para iniciar os serviços Docker (back-end, front-end e banco de dados)
up:
	docker-compose up -d

# Tarefa para parar e remover os serviços Docker
down:
	docker-compose down

# Tarefa para reiniciar os serviços Docker
restart: down build up

# Tarefa para exibir os logs dos serviços Docker
logs:
	docker-compose logs

# Tarefa para acessar o terminal interativo do contêiner do back-end
backend:
	docker-compose exec backend bash

# Tarefa para acessar o terminal interativo do contêiner do front-end
frontend:
	docker-compose exec frontend sh

# Tarefa para acessar o terminal interativo do contêiner do banco de dados
db:
	docker exec -it $(CONTAINER_DB) mysql -u usuario_db -p

# Tarefa para listar os containers em execução
ps:
	docker-compose ps -a

# Tarefa para limpar imagens e volumes desnecessários
clean:
	docker-compose down -v
	docker system prune -f

# Tarefa para migrar o banco de dados
migrate:
	docker-compose exec backend python manage.py migrate

# Tarefa para criar e aplicar migrações no banco de dados
makemigrations:
	docker-compose exec backend python manage.py makemigrations

# Tarefa para rodar os testes do back-end
test-backend:
	docker-compose exec backend python manage.py test

# Tarefa para rodar os testes do front-end
test-frontend:
	docker-compose exec frontend npm test

# Tarefa para construir a aplicação Angular
build-frontend:
	docker-compose exec frontend npm run build
