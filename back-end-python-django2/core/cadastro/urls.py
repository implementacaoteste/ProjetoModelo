# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.usuario_view import UsuarioViewSet
from .views.candidato_view import CandidatoViewSet

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename = 'usuario')
router.register(r'candidato', CandidatoViewSet, basename='candidato')

urlpatterns = [
    path('', include(router.urls)),
]