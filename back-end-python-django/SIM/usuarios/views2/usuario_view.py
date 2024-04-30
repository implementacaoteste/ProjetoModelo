from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import Usuario
from ..serializers.usuario_serializer import UsuarioSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    @swagger_auto_schema(operation_description="Buscar todos os usuários")
    def buscar_todos(request):
        """
        Lista todos os usuários
        """
        usuario_list = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario_list, many=True)
        return Response(usuario_serializer.data)

@api_view(['GET'])
@swagger_auto_schema(operation_description="Busca um usuário por id")
def buscar_por_id(request, pk):
    """
    Busca um usuário por id.
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    usuario_serializer = UsuarioSerializer(usuario)
    return Response(usuario_serializer.data)

@api_view(['POST'])
@swagger_auto_schema(operation_description="Inserir um novo usuário")
def inserir(request):
    """
    Adicionar um novo usuário
    """
    usuario_serializer = UsuarioSerializer(data=request.data)
    if usuario_serializer.is_valid():
        usuario_serializer.save()
        return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
    return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@swagger_auto_schema(operation_description="Altera um usuário existente")
def alterar(request, pk):
    """
    Atualiza um usuário
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    usuario_serializer = UsuarioSerializer(usuario, data=request.data)
    if usuario_serializer.is_valid():
        usuario_serializer.save()
        return Response(usuario_serializer.data)
    return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@swagger_auto_schema(operation_description="Excluir um usuário por id")
def excluir(request, pk):
    """
    Exclui um usuáriopor id
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
