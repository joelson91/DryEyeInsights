from django.urls import path
from core import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('participantes/', views.ver_participantes, name='ver_participantes'),
    path('novo-participante/', views.criar_participante, name='criar_participante'),
    path('detalhes/<int:id_participante>/', views.detalhe_participante, name='detalhes_participante'),
    path('editar-participante/<int:id_participante>/', views.editar_participante, name='editar_participante'),
    path('excluir-participante<int:id_participante>', views.excluir_participante, name='excluir_participante'),
    path('questionario/<int:id_participante>/', views.aplicar_questionario, name='aplicar_questionario'),
    path('ver-questionario/<int:id_participante>/', views.ver_questionario, name='ver_questionario'),
    path('editar_questionario<int:id_questionario>/', views.editar_questionario, name='editar_questionario'),
    path('excluir-questionario<int:id_questionario>', views.excluir_questionario, name='excluir_questionario'),
]
