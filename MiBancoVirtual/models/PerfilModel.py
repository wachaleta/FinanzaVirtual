from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

class Perfil(models.Model):
    """ Perfiles de usuario para crear Cuentas """

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    saldo = models.DecimalField(default=0, editable=False, max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def calcular_saldo(self):
        from MiBancoVirtual.models.SubcuentaModel import Subcuenta
        lista_subcuentas = Subcuenta.objects.filter(perfil=self)

        self.saldo = 0
        for x in lista_subcuentas:
            self.saldo += x.saldo

        self.save()