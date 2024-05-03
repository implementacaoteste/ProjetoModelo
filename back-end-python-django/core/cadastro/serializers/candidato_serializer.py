from rest_framework import serializers
from ..models.candidato import Candidato

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'
