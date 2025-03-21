from django import forms
from core.models import Participante, Questionario


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = [
            'nome',
            'genero',
            'dt_nascimento',
            'email',
            'telefone',
            'endereco'
        ]
        widgets = {
            'dt_nascimento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'telefone': forms.TextInput(attrs={'type': 'tel'}),
        }


class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = [
            'duracao_sono',
            'qualidade_sono',
            'nivel_estresse',
            'pressao_arterial',
            'frequencia_cardiaca',
            'atividade_fisica',
            'consumo_cafeina',
            'consumo_alcool',
            'tabagismo',
            'problema_medico',
            'tomando_medicacao',
            'uso_smartphone',
            'tempo_medio_tela',
            'filtro_luz_azul',
            'fadiga_ocular',
            'vermelhidao_ocular',
            'irritacao_ocular',
        ]
