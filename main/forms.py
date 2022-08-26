from django import forms


class PessoaRecadoForm(forms.Form):
    nome_familia = forms.CharField(required=True, label="Digite o seu nome ou da sua familia", max_length=256)
    recado_familia = forms.CharField(required=True, label="Deixe o reacado para nossa família!", max_length=500)
    