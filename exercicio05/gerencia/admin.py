from django.contrib import admin
from .models import Postagens, Usuario, Categoria, Autor, Comentario

admin.site.register(Postagens)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Comentario)