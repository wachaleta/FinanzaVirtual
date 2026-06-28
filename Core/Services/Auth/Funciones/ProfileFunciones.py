from dateutil.relativedelta import relativedelta
from datetime import date

from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth import models

@transaction.atomic()
def profile_crear(
    usuario: User = None,
):
    fecha_limite_permitida = date.today() + relativedelta(months=1)
    
    profile = models.Profile(
        usuario = usuario,
        nombre = usuario.username,
        fecha_limite_permitida = fecha_limite_permitida,
    )

    profile.full_clean()
    profile.save()

    return profile

@transaction.atomic()
def profile_validar_pago(
    usuario: User = None,
):
    profile = models.Profile.objects.filter(usuario=usuario).first()

    if not profile:
        raise BadRequestException("El usuario no cuenta con un registro profile")

    if profile.fecha_limite_permitida < timezone.localdate():
        raise BadRequestException("No puede ejecutar esta acción. Verifique su pago")

    return profile