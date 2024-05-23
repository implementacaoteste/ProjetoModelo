# ./src/apps/cadastro/data/produto_data.py

from ..models.produto import Produto

class ProdutoData:
	@staticmethod
	def inserir(data):
		return Produto.objects.create(**data)

	@staticmethod
	def buscar_todos():
		return Produto.objects.all()

	@staticmethod
	def buscar_por_id(id):
		return Produto.objects.get(id=id)

	@staticmethod
	def alterar(produto, data):
		for attr, value in data.items():
			setattr(produto, attr, value)
		produto.save()
		return produto

	@staticmethod
	def excluir(produto):
		produto.delete()
