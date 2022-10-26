from django.contrib import admin
from filme.models import Filme
# Register your models here.

class FilmeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano_lancamento','valor_locacao']
    search_fields = ('titulo',)

admin.site.register(Filme, FilmeAdmin)