from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sigla_modalidade = models.CharField(max_length=7)
    curso = models.CharField(max_length=150)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    convocado = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
