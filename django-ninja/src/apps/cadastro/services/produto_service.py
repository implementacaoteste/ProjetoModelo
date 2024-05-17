# ./src/apps/cadastro/services/produto_service.py

from ..data.produto_data import ProdutoData

class ProdutoService:
	@staticmethod
	def inserir(data):
		return ProdutoData.inserir(data)

	@staticmethod
	def buscar_todos():
		return ProdutoData.buscar_todos()

	@staticmethod
	def buscar_por_id(id):
		return ProdutoData.buscar_por_id(id)

	@staticmethod
	def alterar(id, data):
		produto = ProdutoData.buscar_por_id(id)
		return ProdutoData.alterar(produto, data)

	@staticmethod
	def excluir(id):
		produto = ProdutoData.buscar_por_id(id)
		ProdutoData.excluir(produto)
