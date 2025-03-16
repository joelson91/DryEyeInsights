from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import date

GENERO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'))

QUALIDADE_SONO_CHOICES = [
    (1, 'Muito Baixa (Noites muito ruins, sono insatisfatório)'),
    (2, 'Baixa (Acordo frequentemente cansado)'),
    (3, 'Média (Tenho um sono razoável, mas poderia ser melhor)'),
    (4, 'Alta (Durmo bem na maioria das noites)'),
    (5, 'Muito Alta (Sono excelente, acordo revigorado)'),
]

NIVEL_ESTRESSE_CHOICES = [
    (1, 'Muito Baixo (Me sinto completamente relaxado)'),
    (2, 'Baixo (Me sinto tranquilo na maior parte do tempo)'),
    (3, 'Médio (Algum estresse, mas controlável)'),
    (4, 'Alto (Me sinto frequentemente sobrecarregado)'),
    (5, 'Muito Alto (Estresse constante, difícil de lidar)'),
]

PHONE_VALIDATOR = [RegexValidator(regex=r'^\d{10,11}$', message='Telefone inválido')]


class Pesquisador(models.Model):
    id_pesquisador = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    genero = models.CharField(choices=GENERO_CHOICES, max_length=1, verbose_name='Gênero')
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(
        max_length=11,
        validators=[RegexValidator(regex=r'^\d{11}$', message='CPF inválido')],
        unique=True,
        verbose_name='CPF'
    )
    email = models.EmailField(unique=True, verbose_name='Email')
    telefone = models.CharField(
        max_length=11,
        validators=PHONE_VALIDATOR,
        unique=True,
        verbose_name='Telefone'
    )
    instituicao = models.CharField(max_length=100, verbose_name='Instituição')
    dt_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'pesquisador'
        verbose_name = 'Pesquisador'
        verbose_name_plural = 'Pesquisadores'
        ordering = ['nome']


class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    id_pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE, verbose_name='Pesquisador')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    genero = models.CharField(choices=GENERO_CHOICES, max_length=1, verbose_name='Gênero')
    dt_nascimento = models.DateField(verbose_name='Data de nascimento')
    email = models.EmailField(verbose_name='Email', unique=True)
    telefone = models.CharField(
        max_length=11,
        validators=PHONE_VALIDATOR,
        unique=True,
        verbose_name='Telefone'
    )
    endereco = models.CharField(max_length=256, verbose_name='Endereço')
    dt_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')
    status_questionario = models.BooleanField(default=False, verbose_name='Status de questionario')

    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.dt_nascimento.year - (
                (hoje.month, hoje.day) < (self.dt_nascimento.month, self.dt_nascimento.day))
        return idade

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'participante'
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['nome']


class Questionario(models.Model):
    id_questionario = models.AutoField(primary_key=True)
    id_pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE)
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    dt_envio = models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')
    duracao_sono = models.FloatField(verbose_name='Duração do sono')
    qualidade_sono = models.IntegerField(choices=QUALIDADE_SONO_CHOICES, verbose_name='Qualidade do sono')
    nivel_estresse = models.IntegerField(choices=NIVEL_ESTRESSE_CHOICES, verbose_name='Nível de estresse')
    pressao_arterial = models.CharField(max_length=20, verbose_name='Pressão sanguínea')
    frequencia_cardiaca = models.IntegerField(verbose_name='Frequência de cardíaca')
    atividade_fisica = models.IntegerField(verbose_name='Atividade Física')
    consumo_cafeina = models.BooleanField(verbose_name='Consome cafeína')
    consumo_alcool = models.BooleanField(verbose_name='Consome álcool')
    tabagismo = models.BooleanField(verbose_name='Fumante')
    problema_medico = models.BooleanField(verbose_name='Probelma médico')
    tomando_medicacao = models.BooleanField(verbose_name='Tomando medicação')
    uso_smartphone = models.BooleanField(verbose_name='Usa smartphone')
    tempo_medio_tela = models.FloatField(verbose_name='Tempo médio de tela')
    filtro_luz_azul = models.BooleanField(verbose_name='Filtro de luz azul')
    fadiga_ocular = models.BooleanField(verbose_name='Fadiga ocular')
    vermelhidao_ocular = models.BooleanField(verbose_name='Vermelhidão ocular')
    irritacao_ocular = models.BooleanField(verbose_name='Irritação ocular')
    chance_doenca = models.FloatField(verbose_name='Chance de docença')

    def __str__(self):
        return f'Questionário {self.id_questionario} - Pesquisador: {self.id_pesquisador.nome}'

    class Meta:
        db_table = 'questionario'
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'
        ordering = ['id_questionario']
