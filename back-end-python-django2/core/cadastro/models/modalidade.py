from django.db import models

class Modalidade(models.Model):
    """
    teste
    """
    sigla = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=150, unique=True)
    sequencia = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.sigla
