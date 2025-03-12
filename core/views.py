from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Participante, Pesquisador, Questionario
from core.forms import ParticipanteForm, QuestionarioForm


def index(request):
    return render(request, 'index.html')


@login_required
def painel(request):
    pesquisador = Pesquisador.objects.get(user=request.user)
    return render(request, 'painel/painel.html', {'pesquisador': pesquisador})


@login_required
def criar_participante(request):
    pesquisador = get_object_or_404(Pesquisador, user=request.user)

    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            questionario = form.save(commit=False)
            questionario.id_pesquisador = pesquisador
            questionario.save()
            return redirect('painel')
    else:
        form = ParticipanteForm()
        return render(request, 'painel/registro_participante.html', {'form': form})


@login_required
def ver_participantes(request):
    pesquisador_id = get_object_or_404(Pesquisador, user=request.user)
    participantes = Participante.objects.filter(id_pesquisador=pesquisador_id)
    context = {'participantes': participantes}
    return render(request, 'painel/lista_participantes.html', context=context)


@login_required
def detalhe_participante(request, id_participante):
    participante = get_object_or_404(Participante, pk=id_participante, id_pesquisador__user=request.user)
    questionario_preenchido = Questionario.objects.filter(id_participante=participante).exists()

    context = {
        'participante': participante,
        'questionario_preenchido': questionario_preenchido,
    }

    return render(request, 'painel/detalhe_participante.html', context=context)


@login_required
def editar_participante(request, id_participante):
    participante = get_object_or_404(Participante, pk=id_participante)

    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = ParticipanteForm(instance=participante)

    return render(request, 'painel/registro_participante.html', {'form': form})


@login_required
def aplicar_questionario(request, id_participante):
    form = QuestionarioForm()

    pesquisador = get_object_or_404(Pesquisador, user=request.user)
    participante = get_object_or_404(Participante, pk=id_participante)

    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            questionario = form.save(commit=False)
            questionario.id_pesquisador = pesquisador
            questionario.id_participante = participante
            questionario.save()
            return redirect(detalhe_participante, id_participante)
    else:
        return render(request, 'painel/questionario.html', {'form': form})


@login_required
def ver_questionario(request, id_participante):
    questionario = get_object_or_404(Questionario, id_participante=id_participante)
    return render(request, 'painel/ver_questionario.html', {'questionario': questionario})
