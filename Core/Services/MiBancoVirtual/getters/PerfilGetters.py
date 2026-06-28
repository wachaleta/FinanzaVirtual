from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, Subquery, OuterRef
from django.db.transaction import atomic

from Core.Services.MiBancoVirtual import models

@atomic()
def obtener_perfiles_usuario(
    usuario: User = None,
    searchText: str = None,
    activo: bool = None,
):
    perfiles = models.Perfil.objects.filter(usuario=usuario)

    # if activo is not None:
        # perfiles = perfiles.filter(activo=activo)

    if searchText:
        perfiles = perfiles.filter(nombre__icontains=searchText)

    perfiles = perfiles.annotate(
        saldo=Coalesce(
                Subquery(
                    models.Transaccion.objects.filter(
                        perfil_beneficiario=OuterRef('id')
                    ).values('perfil_beneficiario').annotate(
                        total=Sum('monto')
                    ).values('total')
                ), Decimal(0)
            )
            - Coalesce(
                Subquery(
                    models.Transaccion.objects.filter(
                        perfil_ordenante=OuterRef('id')
                    ).values('perfil_ordenante').annotate(
                        total=Sum('monto')
                    ).values('total')
                ), Decimal(0)
            )
    ).order_by('nombre')

    return perfiles