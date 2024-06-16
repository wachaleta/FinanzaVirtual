from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete

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
    
    def save(self, *args, **kwargs):
        
        if self.descripcion == None or self.descripcion == "":
            self.descripcion = "%s transfirió Q%s a %s"% (self.ordenante, self.monto, self.beneficiario)
        
        try:

            Transferencia.objects.get(id=self.id)            

        except:

            if(self.ordenante.saldo >= self.monto):

                self.ordenante.crear_transferencia(self.beneficiario, self.monto)

            else:

                CuentaDeuda.objects.create(
                    saldo = self.monto - self.ordenante.saldo,
                    nombre = "Nueva cuenta de deuda",
                    acreedor = Perfil.objects.get(id=22),
                    deudor = self.ordenante.perfil
                )

                self.ordenante.saldo = 0
                self.ordenante.save()
            

        super().save(*args, **kwargs)

@receiver(pre_save, sender=Transferencia)
def Transferencia_pre_save(sender, instance, **kwargs):

    try:
        instance.PreSaveObject = Transferencia.objects.get(id=instance.id)

    except:
        instance.PreSaveObject = instance

@receiver(post_save, sender=Transferencia)
def Transferencia_post_save(sender, instance, **kwargs):

    #   Detecta si hay un cambio en la transferencia para guardar solo cuando haya un cambio
    if instance.PreSaveObject.ordenante != instance.ordenante or instance.PreSaveObject.beneficiario != instance.beneficiario or instance.PreSaveObject.monto != instance.monto:
        
        if instance.descripcion == "%s transfirió Q%s a %s"% (instance.PreSaveObject.ordenante, instance.PreSaveObject.monto, instance.PreSaveObject.beneficiario):

            descripcion = "%s transfirió Q%s a %s"% (instance.ordenante, instance.monto, instance.beneficiario)
        
        else:
            descripcion = instance.descripcion

        instance.PreSaveObject.ordenante.crear_ingreso(instance.PreSaveObject.monto)
        instance.PreSaveObject.beneficiario.crear_gasto(instance.PreSaveObject.monto)
        instance = Transferencia.objects.get(id=instance.id)
        instance.ordenante.crear_gasto(instance.monto)
        instance.beneficiario.crear_ingreso(instance.monto)
        instance.descripcion = descripcion

        instance.save()

@receiver(pre_delete, sender=Transferencia)
def Transferencia_pre_delete(sender, instance, **kwargs):

    if instance.beneficiario != None:
        instance.beneficiario.crear_transferencia(instance.ordenante, instance.monto)

class CuentaDeuda(models.Model):
    """ Cuenta que se crea para gestionar las deudas o préstamos entre perfiles """
    
    id = models.AutoField(primary_key=True, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=50)
    acreedor = models.ForeignKey(Perfil, related_name="Acreedor", on_delete=models.PROTECT)
    deudor = models.ForeignKey(Perfil, related_name="Deudor", on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
