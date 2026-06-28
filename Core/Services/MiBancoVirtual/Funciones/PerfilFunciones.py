from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def perfil_crear(
    usuario: User = None,
    SumaDisponible: bool = True,
    Nombre: str = None,
) -> models.Perfil:
    ProfileFunciones.profile_validar_pago(usuario=usuario)
    
    perfil = models.Perfil(
        IdUsuario = usuario,
        Nombre = Nombre,
        SumaDisponible = SumaDisponible,
    )

    perfil.full_clean()
    perfil.save()

    return perfil

@transaction.atomic()
def perfil_editar(
    usuario: User = None,
    perfil: models.Perfil = None,
    suma_disponible: bool = True,
    nombre: str = None,
    activo: bool = True
) -> models.Perfil:
    ProfileFunciones.profile_validar_pago(usuario=usuario)
    
    if not perfil:
        raise BadRequestException("No se proporcionó ningún perfil para editar")

    perfil.nombre = nombre
    perfil.suma_disponible = suma_disponible
    perfil.activo = activo

    perfil.full_clean()
    perfil.save()

    return perfil

@transaction.atomic()
def perfil_inactivar(
    usuario: User = None,
    perfil: models.Perfil = None,
):
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not perfil: 
        raise BadRequestException('No se proporcionó ningún perfil para inactivar')

    if perfil.Saldo != 0:
        raise BadRequestException("Este perfil aún tiene saldo")

    perfil.Activo = False

    perfil.save()

    return perfil