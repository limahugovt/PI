from typing import Any

from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    senha = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=255, blank=False)
    autor = models.CharField(max_length=255, blank=False)
    ano = models.IntegerField()
    genero = models.CharField(max_length=255, blank=False)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    livros = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usurio = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.livros) + " " + str(self.usurio)


class Avaliacao(models.Model):
    pontuacao = models.IntegerField()
    comentarios = models.CharField(max_length=255, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario) + " " + str(self.livro)
