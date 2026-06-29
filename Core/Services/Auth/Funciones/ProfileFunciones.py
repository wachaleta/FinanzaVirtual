from dateutil.relativedelta import relativedelta
from datetime import date

from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth import models
from Core.Services.Auth.getters import ProfileGetters
from Core.Services.catalogos.getters import UnidadMonetariaGetters

@transaction.atomic()
def profile_crear(
    usuario: User = None,
):
    fecha_limite_permitida = date.today() + relativedelta(months=1)
    
    unidad_monetaria = UnidadMonetariaGetters.obtener_unidad_monetaria_por_simbolo(simbolo="Q")
    
    profile = models.Profile(
        usuario = usuario,
        nombre = usuario.username,
        fecha_limite_permitida = fecha_limite_permitida,
        unidad_monetaria=unidad_monetaria,
    )

    profile.full_clean()
    profile.save()

    return profile

@transaction.atomic()
def profile_validar_pago(
    usuario: User = None,
):
    profile = ProfileGetters.obtener_profile_por_usuario(usuario=usuario)

    if profile.fecha_limite_permitida < timezone.localdate():
        raise BadRequestException("No puede ejecutar esta acción. Verifique su pago")

    return profile