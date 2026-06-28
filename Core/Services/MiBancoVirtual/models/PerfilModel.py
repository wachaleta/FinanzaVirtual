from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    """ Perfiles de usuario para crear Cuentas """

    id = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    suma_disponible = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    def __int__(self):
        return self.id
    
    class Meta:
        db_table="perfil"