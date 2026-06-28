from decimal import Decimal

from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def cuenta_crear(
    usuario: User = None,
    nombre: str = None,
    es_efectivo: bool = False,
    saldo_real: int = 0,
    bQ100: int = 0,
    bQ50: int = 0,
    bQ20: int = 0,
    bQ10: int = 0,
    bQ5: int = 0,
    m100c: int = 0,
    m50c: int = 0,
    m25c: int = 0,
    m10c: int = 0,
    m5c: int = 0,
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    cuenta = models.Cuenta(
        usuario = usuario,
        nombre = nombre,
        es_efectivo = es_efectivo,
        saldo_real = saldo_real,
        bQ100 = bQ100,
        bQ50 = bQ50,
        bQ20 = bQ20,
        bQ10 = bQ10,
        bQ5 = bQ5,
        m100c = m100c,
        m50c = m50c,
        m25c = m25c,
        m10c = m10c,
        m5c = m5c,
    )

    cuenta.full_clean()
    cuenta.save()

    return cuenta

@transaction.atomic()
def cuenta_editar(
    usuario: User = None,
    cuenta: models.Cuenta = None,
    nombre: str = None,
    es_efectivo: bool = False,
    activo: bool = False,
    saldo_real: Decimal = 0,
    bQ100: int = 0,
    bQ50: int = 0,
    bQ20: int = 0,
    bQ10: int = 0,
    bQ5: int = 0,
    m100c: int = 0,
    m50c: int = 0,
    m25c: int = 0,
    m10c: int = 0,
    m5c: int = 0,
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not cuenta:
        raise BadRequestException("No se proporcionó ninguna cuenta para editar")

    cuenta.nombre = nombre
    cuenta.es_efectivo = es_efectivo
    cuenta.saldo_real = saldo_real
    cuenta.activo = activo
    cuenta.bQ100 = bQ100
    cuenta.bQ50 = bQ50
    cuenta.bQ20 = bQ20
    cuenta.bQ10 = bQ10
    cuenta.bQ5 = bQ5
    cuenta.m100c = m100c
    cuenta.m50c = m50c
    cuenta.m25c = m25c
    cuenta.m10c = m10c
    cuenta.m5c = m5c

    # cuenta.full_clean()
    cuenta.save()

    return cuenta

@transaction.atomic()
def cuenta_inactivar(
    usuario: User = None,
    cuenta: models.Cuenta = None,
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not cuenta:
        raise BadRequestException('No se proporcionó ninguna cuenta para inactivar')

    if cuenta.saldo_total != 0:
        raise BadRequestException("Esta cuenta aún tiene saldo")

    cuenta.activo = False

    cuenta.save()