# ./src/apps/restaurante/services/atendente_service.py

from ..data.atendente_data import AtendenteData

class AtendenteService:
	@staticmethod
	def inserir(data):
		return AtendenteData.inserir(data)

	@staticmethod
	def buscar_todos():
		return AtendenteData.buscar_todos()

	@staticmethod
	def buscar_por_id(id):
		return AtendenteData.buscar_por_id(id)

	@staticmethod
	def alterar(id, data):
		atendente = AtendenteData.buscar_por_id(id)
		return AtendenteData.alterar(atendente, data)

	@staticmethod
	def excluir(id):
		atendente = AtendenteData.buscar_por_id(id)
		AtendenteData.excluir(atendente)
