# views.py

from rest_framework import viewsets
from .models import Usuario
from rest_framework.response import Response
from usuarios.serializers.usuario_serializer import UsuarioSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Rota de usuário
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    