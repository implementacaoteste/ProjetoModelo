# ./src/apps/restaurante/data/bebida_data.py

from ..models.bebida import Bebida

class BebidaData:
	@staticmethod
	def inserir(data):
		return Bebida.objects.create(**data)

	@staticmethod
	def buscar_todos():
		return Bebida.objects.all()

	@staticmethod
	def buscar_por_id(id):
		return Bebida.objects.get(id=id)

	@staticmethod
	def alterar(bebida, data):
		for attr, value in data.items():
			setattr(bebida, attr, value)
		bebida.save()
		return bebida

	@staticmethod
	def excluir(bebida):
		bebida.delete()
