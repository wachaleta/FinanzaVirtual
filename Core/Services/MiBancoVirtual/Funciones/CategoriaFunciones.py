from django.contrib.auth.models import User
from django.db import transaction  

from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def categoria_crear(
    usuario: User = None,
    nombre: str = None,
):
    categoria = models.Categoria(
        IdUsuario = usuario,
        Nombre = nombre,
    )

    categoria.full_clean()
    categoria.save()

    return categoria