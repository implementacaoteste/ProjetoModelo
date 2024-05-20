# ./src/apps/restaurante/views/prato_view.py

from ninja import Router
from ..schemas.prato_schema import PratoSchema
from ..services.prato_service import PratoService

prato_router = Router()

@prato_router.get("/prato/")
def buscar_todos(request):
	prato_list = PratoService.buscar_todos()
	return [PratoSchema.from_orm(prato) for prato in prato_list]

@prato_router.post("/prato/")
def inserir(request, prato: PratoSchema):
	prato = PratoService.inserir(prato.dict())
	return PratoSchema.from_orm(prato)

@prato_router.get("/prato/{id}")
def buscar_por_id(request, id: int):
	prato = PratoService.buscar_por_id(id)
	return PratoSchema.from_orm(prato)

@prato_router.put("/prato/{id}")
def alterar(request, id: int, prato: PratoSchema):
	prato = PratoService.alterar(id, prato.dict())
	return PratoSchema.from_orm(prato)

@prato_router.delete("/prato/{id}")
def excluir(request, id: int):
	PratoService.excluir(id)
	return {"message": "Registro excluído com sucesso!"}
