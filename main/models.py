from django.db import models


class PessoaRecado(models.Model):
    nome_familia = models.CharField(max_length=256)
    recado = models.CharField(max_length=500)
     
 
