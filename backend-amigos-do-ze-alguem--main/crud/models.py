from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Beneficiario(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_registro = models.DateField(default=timezone.now)
    observacoes = models.TextField(null=True)

    def __str__(self):
        return self.nome


class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
