import uuid
from django.db import models

from .CuentaModel import Cuenta
from Core.Services.catalogos.models import EfectivoMoneda

class CuentaEfectivo(models.Model):
    """ Relación para los tipos de efectivo de una moneda cuando es una cuenta de efectivo """

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)

    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT)
    efectivo_moneda = models.ForeignKey(EfectivoMoneda, on_delete=models.PROTECT)

    cantidad_efectivo = models.PositiveSmallIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    class Meta:
        db_table="cuenta_efectivo"