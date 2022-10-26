from django.contrib import admin
from categoria.models import Categoria
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ('nome',)
admin.site.register(Categoria,CategoriaAdmin)

