from typing import Any
from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.nome

class Postagens(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
 
    def __str__(self):
        return (str(self.categoria) + " " + str(self.autor))
    
class Comentario(models.Model):
    data = models.DateField()
    texto = models.TextField()
    postagem = models.ForeignKey(Postagens, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    