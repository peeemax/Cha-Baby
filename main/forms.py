from django import forms
from .models import PessoaRecado
from django.forms import ModelForm


class PessoaRecadoForm(forms.ModelForm):

    class Meta:
        nome_familia = forms.CharField(required=True, label="Digite o seu nome ou da sua familia", max_length=256)
        recado = forms.CharField(required=True, label="Deixe o reacado para nossa família!", max_length=500)
    