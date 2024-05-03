from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.modalidade import Modalidade
from ..serializers.modalidade_serializer import ModalidadeSerializer

class ModalidadeViewSet(viewsets.ModelViewSet):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer
