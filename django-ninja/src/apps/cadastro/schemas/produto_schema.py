# ./src/apps/cadastro/schemas/produto_schema.py

from ninja import Schema

class ProdutoSchema(Schema):
	descricao: str
	ativo: bool
