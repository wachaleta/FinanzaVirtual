from django.contrib.auth.models import User
from django.db import models

from . import *

class EfectivoMoneda(models.Model):
    """ Unidades de distintos países """

    id = models.AutoField(primary_key=True, unique=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    unidad_monetaria = models.ForeignKey(UnidadMonetaria, on_delete=models.CASCADE)

    class Meta:
        db_table="cat_efectivo_moneda"