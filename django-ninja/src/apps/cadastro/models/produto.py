from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome