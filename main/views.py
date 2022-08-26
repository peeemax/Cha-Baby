from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PessoaRecadoSerializer
from .models import PessoaRecado


class PessoaRecadoView(viewsets.ModelViewSet):
        serializer_class = PessoaRecadoSerializer
        queryset = PessoaRecado.objects.all()
        
