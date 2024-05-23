# ./src/apps/restaurante/models/prato.py

from django.db import models

class Prato(models.Model):
	descricao = models.CharField(max_length=150)
	ativo = models.BooleanField(default=True)

	def __str__(self):
		return self.descricao
