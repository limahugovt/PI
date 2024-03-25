from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Livro)
admin.site.register(Avaliacao)
admin.site.register(Emprestimo)
admin.site.register(Categoria)