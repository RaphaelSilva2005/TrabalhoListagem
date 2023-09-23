# This is a sample Python script.
from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

