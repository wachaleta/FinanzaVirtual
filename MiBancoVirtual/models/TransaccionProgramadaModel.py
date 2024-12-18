from django.db import models

class TransaccionProgramada(models.Model):
    """ Transacción estática para ejecutar frecuentemente """

    #   Llave primaria
    Id = models.AutoField(primary_key=True, unique=True)
    
    #   Monto establecido a pagar
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    #   Comentario de la transacción
    Descripcion = models.CharField(max_length=300, null=True, blank=True)
    
    #   Fecha cuando se deja de pagar
    FechaLimite = models.DateField(auto_now_add=False, null=True)

    #   Cantidad que se espera pagar en total
    MetaCantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    #   Cantidad que se ha abonado en total
    Abonado = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    #   Cuando se creó la transacción programada
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    
    #   Subcuenta de quien se retira el dinero
    Ordenante = models.ForeignKey("MiBancoVirtual.Subcuenta", related_name="MiBancoVirtual.Transaccion.ordenante+", on_delete=models.SET_NULL, null=True)

    #   Subcuenta que recibe el dinero
    Beneficiario = models.ForeignKey("MiBancoVirtual.Subcuenta", related_name="MiBancoVirtual.Transaccion.beneficiario+", on_delete=models.SET_NULL, null=True)
    
    #   Categoría de la transacción
    Categoria = models.ForeignKey("MiBancoVirtual.Categoria", on_delete=models.PROTECT)