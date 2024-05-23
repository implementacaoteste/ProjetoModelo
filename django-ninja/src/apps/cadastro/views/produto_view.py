# ./src/apps/cadastro/views/produto_view.py

from ninja import Router
from ..schemas.produto_schema import ProdutoSchema
from ..services.produto_service import ProdutoService

produto_router = Router()

@produto_router.get("/produto/")
def buscar_todos(request):
	produto_list = ProdutoService.buscar_todos()
	return [ProdutoSchema.from_orm(produto) for produto in produto_list]

@produto_router.post("/produto/")
def inserir(request, produto: ProdutoSchema):
	produto = ProdutoService.inserir(produto.dict())
	return ProdutoSchema.from_orm(produto)

@produto_router.get("/produto/{id}")
def buscar_por_id(request, id: int):
	produto = ProdutoService.buscar_por_id(id)
	return ProdutoSchema.from_orm(produto)

@produto_router.put("/produto/{id}")
def alterar(request, id: int, produto: ProdutoSchema):
	produto = ProdutoService.alterar(id, produto.dict())
	return ProdutoSchema.from_orm(produto)

@produto_router.delete("/produto/{id}")
def excluir(request, id: int):
	ProdutoService.excluir(id)
	return {"message": "Registro excluído com sucesso!"}

