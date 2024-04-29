container = back-end

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

stop:
    docker-compose down

migrate:
    docker-compose exec back-end flask db init
    docker-compose exec $(container) flask db migrate
    docker-compose exec $(container) flask db upgrade

# Regra para exibir ajuda
help:
    @echo "Uso:"
    @echo "  make build       - Construir as imagens do contêiner"
    @echo "  make up          - Iniciar os contêineres da aplicação"
    @echo "  make down        - Parar e remover os contêineres da aplicação"
    @echo "  make restart     - Reiniciar os contêineres da aplicação"
    @echo "  make logs        - Exibir logs do contêiner"
    @echo "  make stop        - Parar e remover os contêineres da aplicação"
    @echo "  make migrate     - Criar e executar as migrações do banco de dados"
    @echo "  make help        - Exibir esta mensagem de ajuda"
