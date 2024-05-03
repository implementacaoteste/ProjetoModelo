# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.usuario_view import UsuarioViewSet
from .views.candidato_view import CandidatoViewSet
from .views.modalidade_view import ModalidadeViewSet


router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename = 'usuario')
router.register(r'candidato', CandidatoViewSet, basename = 'candidato')
router.register(r'modalidade', ModalidadeViewSet, basename = 'modalidade')
urlpatterns = [
    path('', include(router.urls)),
]