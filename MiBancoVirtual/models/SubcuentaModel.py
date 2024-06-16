from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete

class Subcuenta(models.Model):
    """ Cuentas que gestionan el dinero de un usuario dentro de una Cuenta """

    id = models.AutoField(primary_key=True, unique=True)
    saldo = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=50, null=True, blank=True, editable=False)
    perfil = models.ForeignKey("MiBancoVirtual.Perfil", on_delete=models.CASCADE)
    cuenta = models.ForeignKey("MiBancoVirtual.Cuenta", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def crear_gasto(self, monto):
        print("saldo antes de crear el gasto: " + str(self.saldo))

        self.saldo -= monto
        print("saldo después de crear el gasto: " + str(self.saldo))

        self.save()
        self.cuenta.calcular_saldo()
        self.perfil.calcular_saldo()

    def crear_ingreso(self, monto):

        self.saldo += monto
        print("saldo después de crear el ingreso: " + str(self.saldo))
        self.save()
        self.cuenta.calcular_saldo()
        self.perfil.calcular_saldo()

    def crear_transferencia(self, beneficiario, monto):

        self.crear_gasto(monto)
        beneficiario.crear_ingreso(monto)
        
        self.save()
        beneficiario.save()

    def cambiar_nombre(self):
        self.nombre = self.cuenta.nombre + " " + self.perfil.nombre
        self.save()

    def save(self, *args, **kwargs):

        if self.saldo == "":
            self.saldo = 0


        super().save(*args, **kwargs)

@receiver(post_delete, sender=Subcuenta)
def Subcuenta_post_delete(sender, instance, **kwargs):
    instance.cuenta.calcular_saldo()
    instance.perfil.calcular_saldo()
