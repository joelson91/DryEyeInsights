from django.db import models
from django.core.validators import RegexValidator
from datetime import date

GENERO_CHOICES = (('M', 'Masculino'), ('F', 'Feminino'))
PHONE_VALIDATOR = [RegexValidator(regex=r'^\d{10,11}$', message='Telefone inválido')]


class Pesquisador(models.Model):
    id_pesquisador = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f'Questionário {self.id_questionario} - Pesquisador: {self.id_pesquisador.nome}'

    class Meta:
        db_table = 'questionario'
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'
        ordering = ['id_questionario']
