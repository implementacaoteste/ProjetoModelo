# ./src/apps/restaurante/data/prato_data.py

from ..models.prato import Prato

class PratoData:
	@staticmethod
	def inserir(data):
		return Prato.objects.create(**data)

	@staticmethod
	def buscar_todos():
		return Prato.objects.all()

	@staticmethod
	def buscar_por_id(id):
		return Prato.objects.get(id=id)

	@staticmethod
	def alterar(prato, data):
		for attr, value in data.items():
			setattr(prato, attr, value)
		prato.save()
		return prato

	@staticmethod
	def excluir(prato):
		prato.delete()
