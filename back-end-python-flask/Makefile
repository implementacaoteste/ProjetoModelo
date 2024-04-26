# Define a regra padrão
.DEFAULT_GOAL := help
container=back-end

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker logs $(container)
	
# Regra para executar a aplicação usando o Docker Compose
run2:
	docker-compose up --build

# Regra para parar e remover os contêineres da aplicação
stop:
	docker-compose down

# Regra para criar e executar as migrações do banco de dados
migrate:
	docker-compose exec app flask db migrate
	docker-compose exec app flask db upgrade

# Regra para executar testes
test:
	docker-compose exec app pytest

# Regra para exibir ajuda
help:
	@echo "Uso:"
	@echo "  make run         - Executar a aplicação"
	@echo "  make stop        - Parar e remover os contêineres da aplicação"
	@echo "  make migrate     - Criar e executar as migrações do banco de dados"
	@echo "  make test        - Executar testes"
	@echo "  make help        - Exibir esta mensagem de ajuda"


