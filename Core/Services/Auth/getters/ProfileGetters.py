from django.db.transaction import atomic

from Core.Application.Exceptions import BadRequestException

from Core.Services.Auth import models
from Core.Services.Auth.Funciones import ProfileFunciones

@atomic()
def obtener_profile_por_usuario(
    usuario = None
) -> models.Profile:

    if not usuario:
        raise BadRequestException("No se proporcionó ningún usuario para buscar el profile")

    profile = models.Profile.objects.filter(usuario=usuario).first()

    if not profile:
        profile = ProfileFunciones.profile_crear(usuario=usuario)
    
    return profile