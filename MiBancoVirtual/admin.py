from django.contrib import admin
from .models import *

class CuentaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "saldo_total")

class SubcuentaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "saldo", "id")

class GastoAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha", "subcuenta", "categoria", "saldo_actual")

class IngesoAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha", "subcuenta", "categoria", "saldo_actual")

class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ("monto", "descripcion", "fecha", "ordenante", "beneficiario")

# Register your models here.
admin.site.register(Perfil,)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Subcuenta, SubcuentaAdmin)
admin.site.register(Categoria,)
admin.site.register(Gasto, GastoAdmin)
admin.site.register(Ingreso, IngesoAdmin)
admin.site.register(Transferencia, TransferenciaAdmin)