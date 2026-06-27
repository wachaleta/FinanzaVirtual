from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException
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

@transaction.atomic()
def categoria_editar(
    usuario: User = None,
    categoria: models.Categoria = None,
    Nombre: str = None,
    Activo: bool = True,
) -> models.Categoria:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not categoria:
        raise BadRequestException("No se proporcionó ninguna categoría para editar")

    categoria.Nombre = Nombre
    categoria.Activo = Activo

    categoria.full_clean()
    categoria.save()

    return categoria

@transaction.atomic()
def categoria_inactivar(
    usuario: User = None,
    categoria: models.Categoria = None,
) -> models.Categoria:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not categoria:
        raise BadRequestException('No se proporcionó ninguna categoría para inactivar')

    categoria.Activo = False

    categoria.save()

    return categoria