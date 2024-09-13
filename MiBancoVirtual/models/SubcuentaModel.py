from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

class Subcuenta(models.Model):
    """ Cuentas que gestionan el dinero de un usuario dentro de una Cuenta """

    id = models.AutoField(primary_key=True, unique=True)
    perfil = models.ForeignKey("MiBancoVirtual.Perfil", on_delete=models.CASCADE)
    cuenta = models.ForeignKey("MiBancoVirtual.Cuenta", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cuenta} - {self.perfil}"