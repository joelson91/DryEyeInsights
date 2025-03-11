from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Participante, Pesquisador
from core.forms import ParticipanteForm, QuestionarioForm


def index(request):
    return render(request, 'index.html')


@login_required
def painel(request):
    return render(request, 'painel/painel.html')


@login_required
def criar_participante(request):
    form = ParticipanteForm()
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        return render(request, 'painel/registro_participante.html', {'form': form})


@login_required
def ver_participantes(request):
    participantes = Participante.objects.all()
    context = {'participantes': participantes}
    return render(request, 'painel/lista_participantes.html', context=context)


@login_required
def detalhe_participante(request, participante_id):
    dados = Participante.objects.get(id=participante_id)
    pesquisador = request.user.id
    context = {'participante': dados, 'pesquisador': pesquisador}
    render(request, 'painel/detalhe_participante.html', context=context)


@login_required
def aplicar_questionario(request):
    form = QuestionarioForm()

    pesquisador = request.user.id
    participante = request.user.id

    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            questionario = form.save(commit=False)
            questionario.id_pesquisador = pesquisador
            questionario.id_participante = participante
            questionario.save()
            return redirect('painel')
    else:
        render(request, 'painel/questionario.html', {'form': form})
