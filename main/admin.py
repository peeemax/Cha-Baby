from django.contrib import admin
from .models import PessoaRecado

class PessoaRecadoAdmin(admin.ModelAdmin):
    list_display = ("nome_familia", "recado")
 
   
admin.site.register(PessoaRecado, PessoaRecadoAdmin)
