from django.contrib import admin
from .models import Pesquisador, Participante


@admin.register(Pesquisador)
class PesquisadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'email', 'telefone', 'instituicao', 'dt_cadastro')
    list_filter = ('nome', 'genero', 'dt_cadastro')
    search_fields = ('nome', 'genero', 'dt_cadastro')

    def dt_cadastro(self, obj):
        return obj.dt_cadastro

    dt_cadastro.short_description = 'Data de Cadastro'


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    list_filter = ('nome', 'email')
    search_fields = ('nome', 'email')
