from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import CreateView

from main.forms import PessoaRecadoForm

from .serializers import PessoaRecadoSerializer
from .models import PessoaRecado


class PessoaRecadoCreateView(CreateView):
        model = PessoaRecado
        form_class = PessoaRecadoForm
        success_url = ''


class PessoaRecadoView(viewsets.ModelViewSet):
        serializer_class = PessoaRecadoSerializer
        queryset = PessoaRecado.objects.all()
        
