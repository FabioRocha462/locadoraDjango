from django.contrib import admin
from cliente.models import Cliente
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','email','endereco']
    search_field = ('nome',)

admin.site.register(Cliente,ClienteAdmin)