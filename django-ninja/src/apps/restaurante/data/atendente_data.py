# ./src/apps/restaurante/data/atendente_data.py

from ..models.atendente import Atendente

class AtendenteData:
	@staticmethod
	def inserir(data):
		return Atendente.objects.create(**data)

	@staticmethod
	def buscar_todos():
		return Atendente.objects.all()

	@staticmethod
	def buscar_por_id(id):
		return Atendente.objects.get(id=id)

	@staticmethod
	def alterar(atendente, data):
		for attr, value in data.items():
			setattr(atendente, attr, value)
		atendente.save()
		return atendente

	@staticmethod
	def excluir(atendente):
		atendente.delete()
