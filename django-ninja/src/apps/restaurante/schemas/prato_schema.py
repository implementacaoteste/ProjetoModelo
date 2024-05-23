# ./src/apps/restaurante/schemas/prato_schema.py

from ninja import Schema

class PratoSchema(Schema):
	descricao: str
	ativo: bool
