from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

#def painel(request):
#    return render(request, 'painel.html')