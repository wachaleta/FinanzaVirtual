from django.contrib.auth.models import User
from django.db import transaction  

from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def categoria_crear(
    usuario: User = None,
    Nombre: str = None,
) -> models.Categoria:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    categoria = models.Categoria(
        IdUsuario = usuario,
        Nombre = Nombre,
    )

    categoria.full_clean()
    categoria.save()

    return categoria