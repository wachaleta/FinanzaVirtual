from django.db import models

class TransaccionProgramadaDetalle(models.Model):
    """ Detalles de Transacción estática para ejecutar frecuentemente """

    IdTransaccionProgramadaDetalle = models.AutoField(primary_key=True, unique=True)

    TransaccionProgramada = models.ForeignKey("MiBancoVirtual.TransaccionProgramada", on_delete=models.CASCADE)

    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    Descripcion = models.CharField(max_length=300, null=True, blank=True)
    Fecha = models.DateField(auto_now_add=False, default=None)
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    
    IdPerfilOrdenante = models.ForeignKey("MiBancoVirtual.Perfil", related_name="perfil_ordenante", on_delete=models.SET_NULL, null=True)
    IdCuentaOrdenante = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="cuenta_ordenante", on_delete=models.SET_NULL, null=True)

    IdPerfilBeneficiario = models.ForeignKey("MiBancoVirtual.Perfil", related_name="perfil_beneficiario", on_delete=models.SET_NULL, null=True)
    IdCuentaBeneficiaria = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="cuenta_beneficiaria", on_delete=models.SET_NULL, null=True)
    
    IdCategoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)