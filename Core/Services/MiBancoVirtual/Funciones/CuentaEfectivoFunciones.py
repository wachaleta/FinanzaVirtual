from decimal import Decimal

from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models
from Core.Services.catalogos import models as catalogos_models

@transaction.atomic()
def cuenta_efectivo_crear(
    usuario: User = None,
    cuenta: models.Cuenta = None,
    efectivo_moneda: catalogos_models.EfectivoMoneda = None,
    cantidad_efectivo: Decimal = 0,
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    try:
        cantidad_efectivo = Decimal(cantidad_efectivo)
    except:
        cantidad_efectivo = Decimal(0)

    cuenta_efectivo = models.CuentaEfectivo(
        cuenta = cuenta,
        efectivo_moneda = efectivo_moneda,
        cantidad_efectivo = cantidad_efectivo,
        valor_total = Decimal(efectivo_moneda.valor * cantidad_efectivo),
    )

    cuenta_efectivo.full_clean()
    cuenta_efectivo.save()

    return cuenta_efectivo

@transaction.atomic()
def cuenta_efectivo_editar(
    usuario: User = None,
    cuenta_efectivo: models.CuentaEfectivo = None,
    cantidad_efectivo = 0,
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not cuenta_efectivo:
        raise BadRequestException('No se proporcionó el efectivo de la cuenta para editar')
    
    try:
        cantidad_efectivo = Decimal(cantidad_efectivo)
    except:
        cantidad_efectivo = Decimal(0)

    cuenta_efectivo.cantidad_efectivo = cantidad_efectivo
    cuenta_efectivo.valor_total = Decimal(cuenta_efectivo.efectivo_moneda.valor * cantidad_efectivo)

    cuenta_efectivo.save()

    return cuenta_efectivo