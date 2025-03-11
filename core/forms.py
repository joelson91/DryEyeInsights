from django import forms
from core.models import Participante, Questionario


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'
        widgets = {
            'dt_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'telefone': forms.TextInput(attrs={'type': 'tel'}),
        }


class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = '__all__'
