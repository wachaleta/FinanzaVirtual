from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete

class Ingreso(models.Model):
    """ Monto a ingresar en una subcuenta """

    id = models.AutoField(primary_key=True, unique=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False)
    subcuenta = models.ForeignKey("MiBancoVirtual.Subcuenta", on_delete=models.CASCADE)
    categoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)
    saldo_actual = models.DecimalField(editable=False, default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.descripcion)

@receiver(pre_delete, sender=Ingreso)
def Ingreso_pre_delete(sender, instance, **kwargs):

    instance.subcuenta.crear_gasto(instance.monto)
