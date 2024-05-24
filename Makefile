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
	docker-compose -f docker-compose.yml build

# Tarefa para iniciar os serviços Docker (back-end, front-end e banco de dados)
up:
	docker-compose -f docker-compose.yml up -d

# Tarefa para parar e remover os serviços Docker
down:
	docker-compose -f docker-compose.yml down

# Tarefa para reiniciar os serviços Docker
restart: down build up ps

# Tarefa para exibir os logs dos serviços Docker
logs:
	docker-compose -f docker-compose.yml logs

# Tarefa para acessar o terminal interativo do contêiner do back-end
backend:
	docker-compose -f docker-compose.yml exec backend bash

# Tarefa para acessar o terminal interativo do contêiner do front-end
frontend:
	docker-compose -f docker-compose.yml exec frontend sh

# Tarefa para acessar o terminal interativo do contêiner do banco de dados
db:
	docker exec -it $(CONTAINER_DB) mysql -u usuario_db -p

# Tarefa para listar os containers em execução
ps:
	docker-compose -f docker-compose.yml ps -a
	docker images

# Tarefa para limpar imagens e volumes desnecessários
clean:
	docker-compose -f docker-compose.yml down -v
	docker system prune -f

	docker rmi projetomodelo-backend
	docker rmi projetomodelo-frontend
	docker rmi mysql
	rm -rf db_mysql
	python3 django-ninja/scripts/remove_pycache.py
	make ps
	sleep 2
	clear


# Tarefa para migrar o banco de dados
migrate:
	docker-compose -f docker-compose.yml exec backend python manage.py migrate

# Tarefa para criar e aplicar migrações no banco de dados
makemigrations:
	docker-compose -f docker-compose.yml exec backend python manage.py makemigrations

# Tarefa para rodar os testes do back-end
test-backend:
	docker-compose -f docker-compose.yml exec backend python manage.py test

# Tarefa para rodar os testes do front-end
test-frontend:
	docker-compose -f docker-compose.yml exec frontend npm test

# Tarefa para construir a aplicação Angular
build-frontend:
	docker-compose -f docker-compose.yml exec frontend npm run build


