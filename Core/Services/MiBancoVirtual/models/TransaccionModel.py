from django.db import models

from . import *

class Transaccion(models.Model):
    """
    Modelo para el manejo de todas las transacciones
    ordenante: gasto
    beneficiario: ingreso
    ambos: transferencia
    """

    id = models.AutoField(primary_key=True, unique=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    
    perfilOrdenante = models.ForeignKey("MiBancoVirtual.Perfil", related_name="transaccion_perfil_ordenante", on_delete=models.SET_NULL, null=True)
    cuentaOrdenante = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="transaccion_cuenta_ordenante", on_delete=models.SET_NULL, null=True)

    perfilBeneficiario = models.ForeignKey("MiBancoVirtual.Perfil", related_name="transaccion_perfil_beneficiario", on_delete=models.SET_NULL, null=True)
    cuentaBeneficiaria = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="transaccion_cuenta_beneficiaria", on_delete=models.SET_NULL, null=True)
    
    categoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)