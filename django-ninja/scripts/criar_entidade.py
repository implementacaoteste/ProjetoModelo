# ./scripts/criar_entidade.py

import os
import sys

def camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

def criar_entidade(caminho_arquivo, conteudo):
    with open(caminho_arquivo, 'w') as f:
        f.write(conteudo)

def main(nome_app, nome_entidade):
    caminho_base = os.path.join('src', 'apps', nome_app)
    nome_da_classe = camel_case(nome_entidade)

    # Diretórios e arquivos a serem criados
    caminhos_e_conteudos = [
        (os.path.join(caminho_base, 'models', f'{nome_entidade}.py'), 
         f"# ./src/apps/{nome_app}/models/{nome_entidade}.py\n\n"
         "from django.db import models\n\n"
         f"class {nome_da_classe}(models.Model):\n"
         "\t# TODO: Adicione aqui os atributos da classe.\n"
         "\tdescricao = models.CharField(max_length=150)\n"
         "\tativo = models.BooleanField(default=True)\n\n"
         "\tdef __str__(self):\n"
         "\t\treturn self.descricao\n"),

        (os.path.join(caminho_base, 'data', f'{nome_entidade}_data.py'), 
         f"# ./src/apps/{nome_app}/data/{nome_entidade}_data.py\n\n"
         f"from ..models.{nome_entidade} import {nome_da_classe}\n\n"
         f"class {nome_da_classe}Data:\n"
         "\t@staticmethod\n"
         "\tdef inserir(dados):\n"
         f"\t\treturn {nome_da_classe}.objects.create(**dados)\n\n"
         "\t@staticmethod\n"
         "\tdef buscar_todos():\n"
         f"\t\treturn {nome_da_classe}.objects.all()\n\n"
         "\t@staticmethod\n"
         "\tdef buscar_por_id(id):\n"
         f"\t\treturn {nome_da_classe}.objects.get(id=id)\n\n"
         "\t@staticmethod\n"
         f"\tdef alterar({nome_entidade}, dados):\n"
         f"\t\tfor attr, valor in dados.items():\n"
         f"\t\t\tsetattr({nome_entidade}, attr, valor)\n"
         f"\t\t{nome_entidade}.save()\n"
         f"\t\treturn {nome_entidade}\n\n"
         "\t@staticmethod\n"
         f"\tdef excluir({nome_entidade}):\n"
         f"\t\t{nome_entidade}.delete()\n"),

        (os.path.join(caminho_base, 'services', f'{nome_entidade}_service.py'), 
         f"# ./src/apps/{nome_app}/services/{nome_entidade}_service.py\n\n"
         f"from ..data.{nome_entidade}_data import {nome_da_classe}Data\n\n"
         f"class {nome_da_classe}Service:\n"
         "\t@staticmethod\n"
         "\tdef inserir(dados):\n"
         f"\t\treturn {nome_da_classe}Data.inserir(dados)\n\n"
         "\t@staticmethod\n"
         "\tdef buscar_todos():\n"
         f"\t\treturn {nome_da_classe}Data.buscar_todos()\n\n"
         "\t@staticmethod\n"
         "\tdef buscar_por_id(id):\n"
         f"\t\treturn {nome_da_classe}Data.buscar_por_id(id)\n\n"
         "\t@staticmethod\n"
         f"\tdef alterar(id, dados):\n"
         f"\t\t{nome_entidade} = {nome_da_classe}Data.buscar_por_id(id)\n"
         f"\t\treturn {nome_da_classe}Data.alterar({nome_entidade}, dados)\n\n"
         "\t@staticmethod\n"
         f"\tdef excluir(id):\n"
         f"\t\t{nome_entidade} = {nome_da_classe}Data.buscar_por_id(id)\n"
         f"\t\t{nome_da_classe}Data.excluir({nome_entidade})\n"),

        (os.path.join(caminho_base, 'views', f'{nome_entidade}_view.py'), 
         f"# ./src/apps/{nome_app}/views/{nome_entidade}_view.py\n\n"
         "from ninja import Router\n"
         f"from ..schemas.{nome_entidade}_schema import {nome_da_classe}Schema\n"
         f"from ..services.{nome_entidade}_service import {nome_da_classe}Service\n\n"
         f"{nome_entidade}_router = Router()\n\n"
         f"@{nome_entidade}_router.get(\"/{nome_entidade}/\")\n"
         "def buscar_todos(request):\n"
         f"\t{nome_entidade}_lista = {nome_da_classe}Service.buscar_todos()\n"
         f"\treturn [{nome_da_classe}Schema.from_orm({nome_entidade}) for {nome_entidade} in {nome_entidade}_lista]\n\n"
         f"@{nome_entidade}_router.post(\"/{nome_entidade}/\")\n"
         f"def inserir(request, {nome_entidade}: {nome_da_classe}Schema):\n"
         f"\t{nome_entidade} = {nome_da_classe}Service.inserir({nome_entidade}.dict())\n"
         f"\treturn {nome_da_classe}Schema.from_orm({nome_entidade})\n\n"
         f"@{nome_entidade}_router.get(\"/{nome_entidade}/{{id}}\")\n"
         "def buscar_por_id(request, id: int):\n"
         f"\t{nome_entidade} = {nome_da_classe}Service.buscar_por_id(id)\n"
         f"\treturn {nome_da_classe}Schema.from_orm({nome_entidade})\n\n"
         f"@{nome_entidade}_router.put(\"/{nome_entidade}/{{id}}\")\n"
         f"def alterar(request, id: int, {nome_entidade}: {nome_da_classe}Schema):\n"
         f"\t{nome_entidade} = {nome_da_classe}Service.alterar(id, {nome_entidade}.dict())\n"
         f"\treturn {nome_da_classe}Schema.from_orm({nome_entidade})\n\n"
         f"@{nome_entidade}_router.delete(\"/{nome_entidade}/{{id}}\")\n"
         "def excluir(request, id: int):\n"
         f"\t{nome_da_classe}Service.excluir(id)\n\t"
         "return {\"mensagem\": \"Registro excluído com sucesso!\"}\n\n"
         "# TODO: Importar a router no urls.py do core:\n\n"
         f"# from apps.{nome_app}.views.{nome_entidade}_view import {nome_entidade}_router\n\n"
         f"# api.add_router(\"{nome_app}\", {nome_entidade}_router)\n\n"),

        (os.path.join(caminho_base, 'schemas', f'{nome_entidade}_schema.py'), 
         f"# ./src/apps/{nome_app}/schemas/{nome_entidade}_schema.py\n\n"
         "from ninja import Schema\n\n"
         f"class {nome_da_classe}Schema(Schema):\n"
         "\t# TODO: Coloque aqui as colunas do schema.\n"
         "\t# descricao: str\n"
         "\t# ativo: bool\n"
         "\tpass\n")
    ]

    # Cria os diretórios e arquivos com os conteúdos especificados
    for caminho_arquivo, conteudo in caminhos_e_conteudos:
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        criar_entidade(caminho_arquivo, conteudo)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 criar_estrutura_entidade.py <NOME_APP> <NOME_ENTIDADE>")
        sys.exit(1)

    nome_app = sys.argv[1]
    nome_entidade = sys.argv[2]
    main(nome_app, nome_entidade)
