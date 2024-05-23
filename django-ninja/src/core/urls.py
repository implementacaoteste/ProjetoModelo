# ./src/core/urls.py

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from apps.cadastro.views.produto_view import produto_router
from apps.restaurante.views.atendente_view import atendente_router
from apps.restaurante.views.bebida_view import bebida_router
from apps.restaurante.views.prato_view import prato_router

api = NinjaAPI()

api.add_router("cadastro", produto_router)
api.add_router("restaurante", atendente_router)
api.add_router("restaurante", bebida_router)
api.add_router("restaurante", prato_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
