# ./src/apps/restaurante/services/prato_service.py

from ..data.prato_data import PratoData

class PratoService:
	@staticmethod
	def inserir(data):
		return PratoData.inserir(data)

	@staticmethod
	def buscar_todos():
		return PratoData.buscar_todos()

	@staticmethod
	def buscar_por_id(id):
		return PratoData.buscar_por_id(id)

	@staticmethod
	def alterar(id, data):
		prato = PratoData.buscar_por_id(id)
		return PratoData.alterar(prato, data)

	@staticmethod
	def excluir(id):
		prato = PratoData.buscar_por_id(id)
		PratoData.excluir(prato)
