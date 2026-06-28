from django.db import models

class TransaccionProgramadaDetalle(models.Model):
    """ Detalles de Transacción estática para ejecutar frecuentemente """

    id = models.AutoField(primary_key=True, unique=True)

    transaccion_programada = models.ForeignKey("MiBancoVirtual.TransaccionProgramada", on_delete=models.CASCADE)

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    fecha = models.DateField(auto_now_add=False, default=None)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    perfil_ordenante = models.ForeignKey("MiBancoVirtual.Perfil", related_name="trans_prog_det_perfil_ordenante", on_delete=models.SET_NULL, null=True)
    cuenta_ordenante = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="trans_prog_det_cuenta_ordenante", on_delete=models.SET_NULL, null=True)

    perfil_beneficiario = models.ForeignKey("MiBancoVirtual.Perfil", related_name="trans_prog_det_perfil_beneficiario", on_delete=models.SET_NULL, null=True)
    cuenta_beneficiaria = models.ForeignKey("MiBancoVirtual.Cuenta", related_name="trans_prog_det_cuenta_beneficiaria", on_delete=models.SET_NULL, null=True)
    
    categoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)

    class Meta:
        db_table="transaccion_programada_detalle"