from django import forms
from core.models import Participante, Questionario


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'
        widgets = {
            'dt_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
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
            'passos_diarios',
            'atividade_fisica',
            'altura',
            'peso',
            'disturbio_sono',
            'despertares_noturnos',
            'sonolencia_diurna',
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
            'doenca_olho_seco',
        ]
