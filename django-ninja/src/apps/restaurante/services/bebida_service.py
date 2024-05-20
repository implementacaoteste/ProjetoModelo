# ./src/apps/restaurante/services/bebida_service.py

from ..data.bebida_data import BebidaData

class BebidaService:
	@staticmethod
	def inserir(data):
		return BebidaData.inserir(data)

	@staticmethod
	def buscar_todos():
		return BebidaData.buscar_todos()

	@staticmethod
	def buscar_por_id(id):
		return BebidaData.buscar_por_id(id)

	@staticmethod
	def alterar(id, data):
		bebida = BebidaData.buscar_por_id(id)
		return BebidaData.alterar(bebida, data)

	@staticmethod
	def excluir(id):
		bebida = BebidaData.buscar_por_id(id)
		BebidaData.excluir(bebida)
