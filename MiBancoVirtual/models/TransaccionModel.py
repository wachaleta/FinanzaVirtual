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
    # ordenante = models.ForeignKey(Subcuenta, related_name="SubcuentaOrdenante", on_delete=models.SET_NULL, null=True)
    # beneficiario = models.ForeignKey(Subcuenta, related_name="SubcuentaBeneficiaria", on_delete=models.SET_NULL, null=True)
    ordenante = models.ForeignKey("MiBancoVirtual.Subcuenta", related_name="MiBancoVirtual.Transaccion.ordenante+", on_delete=models.SET_NULL, null=True)
    beneficiario = models.ForeignKey("MiBancoVirtual.Subcuenta", related_name="MiBancoVirtual.Transaccion.beneficiario+", on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)