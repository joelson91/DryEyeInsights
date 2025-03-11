from django.urls import path
from core import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('participantes/', views.ver_participantes, name='ver_participantes'),
    path('detalhes/<int:id>/', views.detalhe_participante, name='detalhes_participante'),
    path('novo_participante/', views.criar_participante, name='criar_participante'),
    path('questionario/', views.aplicar_questionario, name='aplicar_questionario'),
]
