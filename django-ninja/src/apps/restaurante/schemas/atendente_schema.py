# ./src/apps/restaurante/schemas/atendente_schema.py

from ninja import Schema

class AtendenteSchema(Schema):
	descricao: str
	ativo: bool