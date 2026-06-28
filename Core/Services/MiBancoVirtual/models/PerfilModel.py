from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from decimal import Decimal

from .TransaccionModel import Transaccion
class Perfil(models.Model):
    """ Perfiles de usuario para crear Cuentas """

    id = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    suma_disponible = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)

    # @property
    # def saldo(self):
    #     saldo_ingresos = Transaccion.objects.filter(IdPerfilBeneficiario = self.id).aggregate(
    #         saldo=Sum('Monto')
    #     )['saldo' or 0]

    #     if(saldo_ingresos == None):
    #         saldo_ingresos = 0

    #     saldo_gastos = Transaccion.objects.filter(IdPerfilOrdenante = self.id).aggregate(
    #         saldo=Sum('Monto')
    #     )['saldo' or 0]

    #     if(saldo_gastos == None):
    #         saldo_gastos = 0
        
    #     saldo_total = round(Decimal(saldo_ingresos - saldo_gastos), 2)

    #     return saldo_total

    def __str__(self):
        return self.nombre
    
    def __int__(self):
        return self.id
    
    class Meta:
        db_table="perfil"