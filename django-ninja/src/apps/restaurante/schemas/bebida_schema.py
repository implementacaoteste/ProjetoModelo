# ./src/apps/restaurante/schemas/bebida_schema.py

from ninja import Schema

class BebidaSchema(Schema):
	descricao: str
	ativo: bool
	pass
