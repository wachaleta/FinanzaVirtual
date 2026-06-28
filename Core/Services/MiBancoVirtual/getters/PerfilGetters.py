from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum
from django.db.transaction import atomic

from Core.Services.MiBancoVirtual import models

@atomic()
def obtener_perfiles_usuario(
    usuario: User = None,
    searchText: str = None,
    activo: bool = None,
):
    perfiles = models.Perfil.objects.filter(usuario=usuario)

    print("activo")
    print(activo)
    if activo is not None:
        perfiles = perfiles.filter(activo=activo)

    if searchText:
        perfiles = perfiles.filter(nombre__icontains=searchText)

    perfiles = perfiles.annotate(
        saldo=Coalesce(
                Sum('transaccion_perfil_beneficiario__Monto'), Decimal(0)
            )-
            Coalesce(
                Sum('transaccion_perfil_ordenante__Monto'), Decimal(0)
            )
    ).order_by('nombre')

    return perfiles