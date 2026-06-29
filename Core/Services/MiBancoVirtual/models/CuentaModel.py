from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from decimal import Decimal

from .TransaccionModel import Transaccion

class Cuenta(models.Model):
    """ Lugar donde está almacenado el dinero """

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo_real = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    es_efectivo = models.BooleanField(default=False)
    bQ100 = models.IntegerField(default=0)
    bQ50 = models.IntegerField(default=0)
    bQ20 = models.IntegerField(default=0)
    bQ10 = models.IntegerField(default=0)
    bQ5 = models.IntegerField(default=0)
    m100c = models.IntegerField(default=0)
    m50c = models.IntegerField(default=0)
    m25c = models.IntegerField(default=0)
    m10c = models.IntegerField(default=0)
    m5c = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table="cuenta"