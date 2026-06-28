from django.db import models
from django.contrib.auth.models import User

class TransaccionProgramada(models.Model):
    """ Transacciones estáticas para ejecutar frecuentemente """

    #   Llave primaria
    id = models.AutoField(primary_key=True, unique=True)
    
    #   Nombre del encabezado
    nombre = models.CharField(max_length=25)
    
    #   Fecha cuando se deja de pagar
    fecha_limite = models.DateField(auto_now_add=False, null=True)

    #   Cuando se creó la transacción programada
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    fecha_ultima_vez = models.DateTimeField(auto_now_add=False, null=True)
    fecha_siguiente_vez = models.DateTimeField(auto_now_add=False, null=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table="transaccion_programada"