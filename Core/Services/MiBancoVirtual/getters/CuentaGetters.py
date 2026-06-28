from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum
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
                Sum('transaccion_cuenta_beneficiaria__monto'), Decimal(0)
            )-
            Coalesce(
                Sum('transaccion_cuenta_ordenante__monto'), Decimal(0)
            )
    ).order_by('nombre')

    return cuentas