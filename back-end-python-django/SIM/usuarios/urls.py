# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.usuario_view import UsuarioViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename = 'usuario')

urlpatterns = [
    path('', include(router.urls)),
]