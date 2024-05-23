# ./src/apps/cadastro/api.py

from ninja import NinjaAPI
from .views.produto_view import produto_router as router_produto

api = NinjaAPI(urls_namespace='cadastro-api')

api.add_router("produto", router_produto)
