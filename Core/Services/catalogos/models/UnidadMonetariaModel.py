from django.contrib.auth.models import User
from django.db import models

class UnidadMonetaria(models.Model):
    """ Unidades de distintos países """

    id = models.CharField(primary_key=True, unique=True)
    nombre_singular = models.CharField(max_length=50)
    nombre_plural = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table="cat_unidad_monetaria"