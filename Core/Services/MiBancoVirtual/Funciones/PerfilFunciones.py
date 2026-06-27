from django.contrib.auth.models import User
from django.db import transaction  

from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def perfil_crear(
    usuario: User = None,
    nombre: str = None,
):
    perfil = models.Perfil(
        IdUsuario = usuario,
        Nombre = nombre,
    )

    perfil.full_clean()
    perfil.save()

    return perfil