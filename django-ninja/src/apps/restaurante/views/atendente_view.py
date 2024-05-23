# ./src/apps/restaurante/views/atendente_view.py

from ninja import Router
from ..schemas.atendente_schema import AtendenteSchema
from ..services.atendente_service import AtendenteService

atendente_router = Router()

@atendente_router.get("/atendente/")
def buscar_todos(request):
	atendente_list = AtendenteService.buscar_todos()
	return [AtendenteSchema.from_orm(atendente) for atendente in atendente_list]

@atendente_router.post("/atendente/")
def inserir(request, atendente: AtendenteSchema):
	atendente = AtendenteService.inserir(atendente.dict())
	return AtendenteSchema.from_orm(atendente)

@atendente_router.get("/atendente/{id}")
def buscar_por_id(request, id: int):
	atendente = AtendenteService.buscar_por_id(id)
	return AtendenteSchema.from_orm(atendente)

@atendente_router.put("/atendente/{id}")
def alterar(request, id: int, atendente: AtendenteSchema):
	atendente = AtendenteService.alterar(id, atendente.dict())
	return AtendenteSchema.from_orm(atendente)

@atendente_router.delete("/atendente/{id}")
def excluir(request, id: int):
	AtendenteService.excluir(id)
	return {"message": "Registro excluído com sucesso!"}

