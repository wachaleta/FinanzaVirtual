from django.db import models

from . import *

class Transaccion(models.Model):
    """
    Modelo para el manejo de todas las transacciones
    ordenante: gasto
    beneficiario: ingreso
    ambos: transferencia
    """

    IdTransaccion = models.AutoField(primary_key=True, unique=True)
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    Descripcion = models.CharField(max_length=300, null=True, blank=True)
    Fecha = models.DateField(auto_now_add=False)
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    
    IdPerfilOrdenante = models.ForeignKey("MiBancoVirtual.Perfil", related_name="transaccion_perfil_ordenante", on_delete=models.SET_NULL, null=True)
    IdCuentaOrdenante = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="transaccion_cuenta_ordenante", on_delete=models.SET_NULL, null=True)

    IdPerfilBeneficiario = models.ForeignKey("MiBancoVirtual.Perfil", related_name="transaccion_perfil_beneficiario", on_delete=models.SET_NULL, null=True)
    IdCuentaBeneficiaria = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="transaccion_cuenta_beneficiaria", on_delete=models.SET_NULL, null=True)
    
    IdCategoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)

    @property
    def CategoriaNombre(self):
        categoria = Categoria.objects.filter(id = self.IdCategoria).first()
        return categoria.nombre