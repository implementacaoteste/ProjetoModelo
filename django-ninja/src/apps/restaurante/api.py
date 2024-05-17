# ./src/apps/restaurante/api.py

from ninja import NinjaAPI
from .views.atendente_view import atendente_router as router_atendente

api = NinjaAPI(urls_namespace='restaurante-api')
api.add_router("atendente", router_atendente)