from decimal import Decimal

from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException

from Core.Services.Auth.Funciones import ProfileFunciones

from Core.Services.catalogos.getters import EfectivoMonedaGetters

from Core.Services.MiBancoVirtual.Funciones import CuentaEfectivoFunciones
from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def cuenta_crear(
    usuario: User = None,
    nombre: str = None,
    es_efectivo: bool = False,
    saldo_real: int = 0,
    efectivo: dict = {}
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    cuenta = models.Cuenta(
        usuario = usuario,
        nombre = nombre,
        es_efectivo = es_efectivo,
        saldo_real = saldo_real,
    )

    cuenta.full_clean()
    cuenta.save()

    if cuenta.es_efectivo:
        efectivo_list = EfectivoMonedaGetters.obtener_efectivo_moneda_por_usuario(usuario=usuario)

        for efectivo_moneda in efectivo_list:

            cantidad = efectivo.get(str(efectivo_moneda.id), Decimal(0))

            CuentaEfectivoFunciones.cuenta_efectivo_crear(
                usuario=usuario,
                cuenta=cuenta,
                efectivo_moneda=efectivo_moneda,
                cantidad_efectivo=cantidad
            )

    return cuenta

@transaction.atomic()
def cuenta_editar(
    usuario: User = None,
    cuenta: models.Cuenta = None,
    nombre: str = None,
    es_efectivo: bool = False,
    activo: bool = False,
    saldo_real: Decimal = 0,
    efectivo: dict = {}
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not cuenta:
        raise BadRequestException("No se proporcionó ninguna cuenta para editar")

    cuenta.nombre = nombre
    cuenta.es_efectivo = es_efectivo
    cuenta.saldo_real = saldo_real
    cuenta.activo = activo

    cuenta.save()

    if cuenta.es_efectivo:
        efectivo_list = EfectivoMonedaGetters.obtener_efectivo_moneda_por_usuario(usuario=usuario)

        for efectivo_moneda in efectivo_list:

            cantidad = efectivo.get(str(efectivo_moneda.id), Decimal(0))
            item = cuenta.cuentaefectivo_set.filter(efectivo_moneda = efectivo_moneda).first()

            print("CANTIDAD 1")
            print(cantidad)
            print(type(cantidad))


            if not item:
                CuentaEfectivoFunciones.cuenta_efectivo_crear(
                    usuario=usuario,
                    cuenta=cuenta,
                    efectivo_moneda=efectivo_moneda,
                    cantidad_efectivo=cantidad
                )
            else:
                CuentaEfectivoFunciones.cuenta_efectivo_editar(
                    usuario=usuario,
                    cuenta_efectivo=item,
                    cantidad_efectivo=cantidad
                )

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