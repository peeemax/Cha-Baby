# import sereliazers from the REST framework
from rest_framework import serializers
  
# import the todo data model
from .models import PessoaRecado
  
# create a sereliazer class
class PessoaRecadoSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = PessoaRecado
        fields = ('id', 'nome_familia','recado')