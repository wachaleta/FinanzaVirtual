from dateutil.relativedelta import relativedelta
from datetime import date

from django.contrib.auth.models import User
from django.db import transaction

from Core.Services.Auth import models

@transaction.atomic()
def profile_crear(
    usuario: User = None,
):
    fecha_limite_permitida = date.today() + relativedelta(months=1)
    
    profile = models.Profile(
        usuario = usuario,
        fecha_limite_permitida = fecha_limite_permitida,
    )

    profile.full_clean()
    profile.save()

    return profile