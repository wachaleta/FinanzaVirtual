from django.contrib.auth.models import User
from django.db import transaction  

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