from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from decimal import Decimal

from .TransaccionModel import Transaccion

class Cuenta(models.Model):
    """ Lugar donde está almacenado el dinero """

    IdCuenta = models.AutoField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=50)
    IdUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    SaldoReal = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    EsEfectivo = models.BooleanField(default=False)
    BQ100 = models.IntegerField(default=0)
    BQ50 = models.IntegerField(default=0)
    BQ20 = models.IntegerField(default=0)
    BQ10 = models.IntegerField(default=0)
    BQ5 = models.IntegerField(default=0)
    M100c = models.IntegerField(default=0)
    M50c = models.IntegerField(default=0)
    M25c = models.IntegerField(default=0)
    M10c = models.IntegerField(default=0)
    M5c = models.IntegerField(default=0)
    Activo = models.BooleanField(default=True)

    @property
    def SaldoTotal(self):
        saldo_ingresos = Transaccion.objects.filter(IdCuentaBeneficiaria = self.IdCuenta).aggregate(
            saldo=Sum('Monto')
        )['saldo' or 0]

        if(saldo_ingresos == None):
            saldo_ingresos = 0

        saldo_gastos = Transaccion.objects.filter(IdCuentaOrdenante = self.IdCuenta).aggregate(
            saldo=Sum('Monto')
        )['saldo' or 0]

        if(saldo_gastos == None):
            saldo_gastos = 0
        
        saldo_total = round(Decimal(saldo_ingresos - saldo_gastos), 2)

        return saldo_total
    
    @property
    def SaldoCalculado(self):
        if self.EsEfectivo:
            saldo =(
                self.BQ100 * 100 +
                self.BQ50 * 50 +
                self.BQ20 * 20 +
                self.BQ10 * 10 +
                self.BQ5 * 5 +
                self.M100c +
                self.M50c * 50 / 100 +
                self.M25c * 25 / 100 +
                self.M10c * 10 / 100 +
                self.M5c * 5 / 100
            )

        else:
            saldo = self.SaldoReal

        return saldo

    def __str__(self):
        return self.Nombre

    def __int__(self):
        return self.IdCuenta