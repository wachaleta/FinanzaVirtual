from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, F, Q, OuterRef, Subquery, Case, When, DecimalField
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
        ),

        saldo_real_calculado = Case(
            When(
                Q(es_efectivo=True),
                then=Subquery(
                    models.CuentaEfectivo.objects.filter(
                        cuenta=OuterRef('id')
                    ).values('cuenta').annotate(
                        total = Sum('valor_total')
                    ).values('total')
                )
            ),
            When(
                Q(es_efectivo=False),
                then=F('saldo_real')
            ),
            default=0,
            output_field=DecimalField()
        )
    ).order_by("nombre")

    return cuentas