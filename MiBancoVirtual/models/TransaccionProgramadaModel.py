from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class TransaccionProgramada(models.Model):
    """ Transacciones estáticas para ejecutar frecuentemente """

    #   Llave primaria
    Id = models.AutoField(primary_key=True, unique=True)
    
    #   Nombre del encabezado
    Nombre = models.CharField(max_length=25)
    
    #   Fecha cuando se deja de pagar
    FechaLimite = models.DateField(auto_now_add=False, null=True)

    #   Cuando se creó la transacción programada
    FechaCreacion = models.DateTimeField(auto_now_add=True)

    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre