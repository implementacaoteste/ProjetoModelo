# ./src/apps/cadastro/schemas/produto_schema.py

from ninja import Schema

class ProdutoSchema(Schema):
    nome: str
    preco: float
    quantidade: int
    ativo: bool
