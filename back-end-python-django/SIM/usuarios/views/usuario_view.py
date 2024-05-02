from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.usuario import Usuario
from ..serializers.usuario_serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        """
        Insere um novo usuário com lógica de negócios personalizada.
        """
        usuario_serializer = self.get_serializer(data=request.data)
        if usuario_serializer.is_valid():
            # Implementar lógica de negócios aqui antes de salvar
            # Por exemplo, verificação de condição ou cálculo adicional
            # Exemplo: Verifica se um usuário com o mesmo e-mail já existe
            email = usuario_serializer.validated_data.get('email')
            if Usuario.objects.filter(email=email).exists():
                return Response({'erro': 'Usuário com este e-mail já existe.'}, status=status.HTTP_400_BAD_REQUEST)

            # Se tudo estiver em conformidade com as regras de negócios, salva o usuário
            self.perform_create(usuario_serializer)
            return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Busca um usuário por ID com lógica de negócios personalizada.
        """
        try:
            usuario = self.get_object()
            # Adicione lógica de negócios aqui se necessário
            # Exemplo: Verifica se o usuário está ativo
            # if not usuario.is_active:
            #     return Response({'erro': 'Usuário está inativo.'}, status=status.HTTP_404_NOT_FOUND)

            usuario_serializer = self.get_serializer(usuario)
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'erro': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """
        Altera um usuário existente com lógica de negócios personalizada.
        """
        try:
            usuario = self.get_object()
            usuario_serializer = self.get_serializer(usuario, data=request.data, partial=True)
            if usuario_serializer.is_valid():
                # Implementar lógica de negócios aqui antes de salvar
                # Exemplo: Verifica se os dados atualizados são válidos
                self.perform_update(usuario_serializer)
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response({'erro': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        Exclui um usuário com lógica de negócios personalizada.
        """
        try:
            usuario = self.get_object()
            # Implementar lógica de negócios aqui antes de excluir
            # Exemplo: Verifica se o usuário pode ser excluído
            self.perform_destroy(usuario)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'erro': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
