# ./src/apps/restaurante/views/bebida_view.py

from ninja import Router
from ..schemas.bebida_schema import BebidaSchema
from ..services.bebida_service import BebidaService

bebida_router = Router()

@bebida_router.get("/bebida/")
def buscar_todos(request):
	bebida_list = BebidaService.buscar_todos()
	return [BebidaSchema.from_orm(bebida) for bebida in bebida_list]

@bebida_router.post("/bebida/")
def inserir(request, bebida: BebidaSchema):
	bebida = BebidaService.inserir(bebida.dict())
	return BebidaSchema.from_orm(bebida)

@bebida_router.get("/bebida/{id}")
def buscar_por_id(request, id: int):
	bebida = BebidaService.buscar_por_id(id)
	return BebidaSchema.from_orm(bebida)

@bebida_router.put("/bebida/{id}")
def alterar(request, id: int, bebida: BebidaSchema):
	bebida = BebidaService.alterar(id, bebida.dict())
	return BebidaSchema.from_orm(bebida)

@bebida_router.delete("/bebida/{id}")
def excluir(request, id: int):
	BebidaService.excluir(id)
	return {"message": "Registro excluído com sucesso!"}

