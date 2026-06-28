import uuid

from django.db import models
from django.contrib.auth.models import User

from Core.Services.catalogos.models import UnidadMonetaria

class Profile(models.Model):
    """ Se utiliza para almacenar otra información de usuario """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(null=True, blank=True)

    ultimo_pago = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_limite_permitida = models.DateField(auto_now=False, auto_now_add=False)

    unidad_monetaria = models.ForeignKey(UnidadMonetaria, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table="profile"