from unittest.util import _MAX_LENGTH
from django.db import models
from categoria.models import Categoria
# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length = 200)
    ano_lancamento = models.IntegerField()
    valor_locacao = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome