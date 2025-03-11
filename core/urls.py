from django.urls import path
from core import views

urlpatterns = [
    path('', views.painel, name='painel'),
]
