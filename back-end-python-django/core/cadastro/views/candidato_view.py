from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.candidato import Candidato
from ..serializers.candidato_serializer import CandidatoSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
