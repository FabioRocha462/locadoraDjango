from django.contrib import admin
from locacao.models import Locacao
# Register your models here.

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ['data_entrega', 'data_locacao','valor']
    search_fields = ('data_locacao',)

admin.site.register(Locacao, LocacaoAdmin)