from django.db import models
from cliente.models import Cliente
from filme.models import Filme
# Create your models here.
class Locacao(models.Model):
    data_entrega = models.DateField()
    data_locacao = models.DateTimeField(auto_now_add=True)
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome