# ./Makefile

IMAGE_NAME = image_python_django
CONTAINER_NAME = container_app

PYTHON = python3
VENV_NAME = env
VENV_DIR = $(CURDIR)/$(VENV_NAME)
PIP = $(VENV_DIR)/bin/pip
ACTIVATE = $(VENV_DIR)/bin/activate

# Tarefa para criar o ambiente virtual
venv:
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

# Tarefa para criar e aplicar migrações no banco de dados
migrate:
	sleep 10
	docker exec $(CONTAINER_NAME) python manage.py makemigrations --no-input
	docker exec $(CONTAINER_NAME) python manage.py migrate --no-input
	docker exec $(CONTAINER_NAME) python manage.py seeds_produto
	@echo "Seeds da entidade Produto criados com sucesso!"

# Tarefa para executar os testes da aplicação
test:
	python manage.py test

# Tarefa para exibir os logs dos serviços Docker
logs:
	docker-compose logs

# Tarefa para acessar o terminal interativo do contêiner da aplicação
app:
	docker-compose exec app bash

ps:
	docker-compose ps -a

mysql:
	docker exec -it container_db mysql -u usuario_db -p

restart: down build up migrate ps

criar:
    # make criar APP_NOME=meu_app
	mkdir -p src/apps/$(APP_NOME)
	mkdir -p src/apps/$(APP_NOME)/data
	mkdir -p src/apps/$(APP_NOME)/management
	mkdir -p src/apps/$(APP_NOME)/management/commands
	mkdir -p src/apps/$(APP_NOME)/models
	mkdir -p src/apps/$(APP_NOME)/schemas
	mkdir -p src/apps/$(APP_NOME)/services
	mkdir -p src/apps/$(APP_NOME)/views
	echo  > src/apps/$(APP_NOME)/__init__.py
	echo "# ./src/apps/$(APP_NOME)/admin.py\n\nfrom django.contrib import admin\n\n# Register your models here." > src/apps/$(APP_NOME)/admin.py
	echo "# ./src/apps/$(APP_NOME)/apps.py\n\nfrom django.apps import AppConfig\n\nclass $(shell echo $(APP_NOME) | sed 's/.*/\u&/')Config(AppConfig):\n\tdefault_auto_field = 'django.db.models.BigAutoField'\n\tname = 'apps.$(APP_NOME)'\n\n# TODO: não esqueça de adicionar o seguinte conteúdo no INSTALLED_APPS do settings.py: 'apps.aplicativo'," > src/apps/$(APP_NOME)/apps.py
	echo "# ./src/apps/$(APP_NOME)/api.py\n\nfrom ninja import NinjaAPI\n#from .views.produto_view import produto_router as router_produto\n\napi = NinjaAPI(urls_namespace='$(APP_NOME)-api')\n#api.add_router("produto", router_produto)" > src/apps/$(APP_NOME)/api.py
	echo "# ./src/apps/$(APP_NOME)/urls.py\n\nfrom django.urls import path, include\nfrom .api import api\n\nurlpatterns = [\n\tpath('', include(api.urls())),\n]" > src/apps/$(APP_NOME)/urls.py
	
criar_entidade:
	# make criar_entidade APP_NOME=aplicativo ENTIDADE_NOME=fornecedor
	echo "# ./src/apps/$(APP_NOME)/models/$(ENTIDADE_NOME).py\n\nfrom django.db import models\n\nclass $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')(models.Model):\n\t# TODO: Adicione aqui os atributos da classe.\n\tdescricao = models.CharField(max_length=150)\n\tativo = models.BooleanField(default=True)\n\n\tdef __str__(self):\n\t\treturn self.descricao" > src/apps/$(APP_NOME)/models/$(ENTIDADE_NOME).py
	echo "# ./src/apps/$(APP_NOME)/data/$(ENTIDADE_NOME)_data.py\n\nfrom ..models.$(ENTIDADE_NOME) import $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')\n\nclass $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data:\n\t@staticmethod\n\tdef inserir(data):\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/').objects.create(**data)\n\n\t@staticmethod\n\tdef buscar_todos():\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/').objects.all()\n\n\t@staticmethod\n\tdef buscar_por_id(id):\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/').objects.get(id=id)\n\n\t@staticmethod\n\tdef alterar($(ENTIDADE_NOME), data):\n\t\tfor attr, value in data.items():\n\t\t\tsetattr($(ENTIDADE_NOME), attr, value)\n\t\t$(ENTIDADE_NOME).save()\n\t\treturn $(ENTIDADE_NOME)\n\n\t@staticmethod\n\tdef excluir($(ENTIDADE_NOME)):\n\t\t$(ENTIDADE_NOME).delete()" > src/apps/$(APP_NOME)/data/$(ENTIDADE_NOME)_data.py
	echo "# ./src/apps/$(APP_NOME)/services/$(ENTIDADE_NOME)_service.py\n\nfrom ..data.$(ENTIDADE_NOME)_data import $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data\n\nclass $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service:\n\t@staticmethod\n\tdef inserir(data):\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.inserir(data)\n\n\t@staticmethod\n\tdef buscar_todos():\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.buscar_todos()\n\n\t@staticmethod\n\tdef buscar_por_id(id):\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.buscar_por_id(id)\n\n\t@staticmethod\n\tdef alterar(id, data):\n\t\t$(ENTIDADE_NOME) = $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.buscar_por_id(id)\n\t\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.alterar($(ENTIDADE_NOME), data)\n\n\t@staticmethod\n\tdef excluir(id):\n\t\t$(ENTIDADE_NOME) = $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.buscar_por_id(id)\n\t\t$(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Data.excluir($(ENTIDADE_NOME))" > src/apps/$(APP_NOME)/services/$(ENTIDADE_NOME)_service.py
	echo "# ./src/apps/$(APP_NOME)/views/$(ENTIDADE_NOME)_view.py\n\nfrom ninja import Router\nfrom ..schemas.$(ENTIDADE_NOME)_schema import $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema\nfrom ..services.$(ENTIDADE_NOME)_service import $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service\n\n$(ENTIDADE_NOME)_router = Router()\n\n@$(ENTIDADE_NOME)_router.get(\"/$(ENTIDADE_NOME)/\")\ndef buscar_todos(request):\n\t$(ENTIDADE_NOME)_list = $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service.buscar_todos()\n\treturn [$(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema.from_orm($(ENTIDADE_NOME)) for $(ENTIDADE_NOME) in $(ENTIDADE_NOME)_list]\n\n@$(ENTIDADE_NOME)_router.post(\"/$(ENTIDADE_NOME)/\")\ndef inserir(request, $(ENTIDADE_NOME): $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema):\n\t$(ENTIDADE_NOME) = $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service.inserir($(ENTIDADE_NOME).dict())\n\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema.from_orm($(ENTIDADE_NOME))\n\n@$(ENTIDADE_NOME)_router.get(\"/$(ENTIDADE_NOME)/{id}\")\ndef buscar_por_id(request, id: int):\n\t$(ENTIDADE_NOME) = $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service.buscar_por_id(id)\n\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema.from_orm($(ENTIDADE_NOME))\n\n@$(ENTIDADE_NOME)_router.put(\"/$(ENTIDADE_NOME)/{id}\")\ndef alterar(request, id: int, $(ENTIDADE_NOME): $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema):\n\t$(ENTIDADE_NOME) = $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service.alterar(id, $(ENTIDADE_NOME).dict())\n\treturn $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema.from_orm($(ENTIDADE_NOME))\n\n@$(ENTIDADE_NOME)_router.delete(\"/$(ENTIDADE_NOME)/{id}\")\ndef excluir(request, id: int):\n\t$(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Service.excluir(id)\n\treturn {\"message\": \"Registro excluído com sucesso!\"}\n\n# TODO: Não esqueça de importar a o $(ENTIDADE_NOME)_router no arquivo ./src/apps/$(APP_NOME)/api.py\n\n#from .views.$(ENTIDADE_NOME)_view import $(ENTIDADE_NOME)_router as router_$(ENTIDADE_NOME)\n\n#api.add_router(\"$(ENTIDADE_NOME)\", router_$(ENTIDADE_NOME))" > src/apps/$(APP_NOME)/views/$(ENTIDADE_NOME)_view.py
	echo "# ./src/apps/$(APP_NOME)/schemas/$(ENTIDADE_NOME)_schema.py\n\nfrom ninja import Schema\n\nclass $(shell echo $(ENTIDADE_NOME) | sed 's/.*/\u&/')Schema(Schema):\n\t# TODO: Coloque aqui as colunas do schema.\n\t# descricao: str\n\t# ativo: bool\n\tpass" > src/apps/$(APP_NOME)/schemas/$(ENTIDADE_NOME)_schema.py

	# TODO: Colocar tarefa mandando importar a router no urls.py do core: from apps.aplicativo.views.fornecedor_view import fornecedor_router

limpar:
	clear
	make down
	docker ps
	docker images
	docker rmi django-ninja-app
	docker rmi mysql
	docker image prune
	docker ps
	docker images
	rm -rf db_mysql
	# rm -rf src/apps/aplicativo/migrations
	sleep 2
	clear