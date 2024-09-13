from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """ Perfiles de usuario para crear Cuentas """

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre