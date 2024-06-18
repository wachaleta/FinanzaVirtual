from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from . import *

class Transferencia(models.Model):
    """ Dinero que se tiene que pasar de una subcuenta a otra """
    id = models.AutoField(primary_key=True, unique=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False)
    ordenante = models.ForeignKey(Subcuenta, related_name="PersonaOrdenante", on_delete=models.SET_NULL, null=True)
    beneficiario = models.ForeignKey(Subcuenta, related_name="PersonaBeneficiaria", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.descripcion)

@receiver(pre_delete, sender=Transferencia)
def Transferencia_pre_delete(sender, instance, **kwargs):

    if instance.beneficiario != None:
        instance.beneficiario.crear_transferencia(instance.ordenante, instance.monto)