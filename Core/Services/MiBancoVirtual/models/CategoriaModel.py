from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    """ Categorías para personalizar las transacciones """
    id = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def __int__(self):
        return self.id
    
    class Meta:
        db_table="categoria"