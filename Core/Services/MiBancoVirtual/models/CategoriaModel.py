from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    """ Categorías para personalizar las transacciones """
    IdCategoria = models.AutoField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=50)
    IdUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def __int__(self):
        return self.id