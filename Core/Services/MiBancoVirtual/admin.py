from django.contrib import admin
from .models import *

# class CuentaAdmin(admin.ModelAdmin):
#     list_display = ("id", "nombre")

class GastoAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha", "categoria", "saldo_actual")

class IngesoAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha", "categoria", "saldo_actual")

class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha")

# Register your models here.
admin.site.register(Perfil,)
# admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Categoria,)