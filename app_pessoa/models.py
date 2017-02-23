from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    data_nascimento = models.DateField()
