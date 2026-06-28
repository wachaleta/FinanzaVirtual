from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, F, Q, OuterRef, Subquery
from django.db.transaction import atomic

from Core.Services.MiBancoVirtual import models

@atomic()
def obtener_cuentas_usuario(
    usuario: User = None,
    searchText: str = None,
    activo: bool = None,
):
    cuentas = models.Cuenta.objects.filter(usuario=usuario)

    if activo is not None:
        cuentas = cuentas.filter(activo=activo)

    if searchText:
        cuentas = cuentas.filter(nombre__icontains=searchText)

    cuentas = cuentas.annotate(
        saldo_total=Coalesce(
            Subquery(
                models.Transaccion.objects.filter(
                    cuenta_beneficiaria=OuterRef('pk')
                ).values('cuenta_beneficiaria').annotate(
                    total=Sum('monto')
                ).values('total')
            ), Decimal(0))
        -Coalesce(
            Subquery(
                models.Transaccion.objects.filter(
                    cuenta_ordenante=OuterRef('pk')
                ).values('cuenta_ordenante').annotate(
                    total=Sum('monto')
                ).values('total')
            ), Decimal(0)
        )
    )

    return cuentas