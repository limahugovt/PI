from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    celular = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Disciplina(models.Model):
    name = models.CharField(max_length=255)
    carga_horaria = models.CharField(max_length=255)
    codigo = models.CharField(max_length=155)

    def __str__(self):
        return self.name
