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

    # @property
    # def saldo_total(self):
    #     saldo_ingresos = Transaccion.objects.filter(cuenta_beneficiaria = self.IdCuenta).aggregate(
    #         saldo=Sum('Monto')
    #     )['saldo' or 0]

    #     if(saldo_ingresos == None):
    #         saldo_ingresos = 0

    #     saldo_gastos = Transaccion.objects.filter(cuenta_ordenante = self.IdCuenta).aggregate(
    #         saldo=Sum('Monto')
    #     )['saldo' or 0]

    #     if(saldo_gastos == None):
    #         saldo_gastos = 0
        
    #     saldo_total = round(Decimal(saldo_ingresos - saldo_gastos), 2)

    #     return saldo_total
    
    @property
    def saldo_efectivo_calculado(self):
        if self.es_efectivo:
            saldo =(
                self.bQ100 * 100 +
                self.bQ50 * 50 +
                self.bQ20 * 20 +
                self.bQ10 * 10 +
                self.bQ5 * 5 +
                self.m100c +
                self.m50c * 50 / 100 +
                self.m25c * 25 / 100 +
                self.m10c * 10 / 100 +
                self.m5c * 5 / 100
            )

        else:
            saldo = self.saldo_real

        return saldo

    def __str__(self):
        return self.Nombre

    def __int__(self):
        return self.IdCuenta
    
    class Meta:
        db_table="cuenta"