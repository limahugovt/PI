from django.db import models


class Aluno(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    mather_name = models.CharField(max_length=255, blank=True)
    cpf = models.IntegerField(max_length=11, blank=False)
    years_old = models.IntegerField(max_length=255, blank=False)
    activity = models.BooleanField()

    def __str__(self):
        return self.name
