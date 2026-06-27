from datetime import date

from django.contrib.auth.models import User
from django.db import transaction  

from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def transaccion_crear(
    usuario: User = None,
    Monto = None,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdPerfilBeneficiario: models.Perfil = None,
    IdCuentaBeneficiaria: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
) -> models.Transaccion:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    transaccion = models.Transaccion(
        Monto = Monto,
        Descripcion = Descripcion,
        Fecha = Fecha,
        IdPerfilOrdenante = IdPerfilOrdenante,
        IdCuentaOrdenante = IdCuentaOrdenante,
        IdPerfilBeneficiario = IdPerfilBeneficiario,
        IdCuentaBeneficiaria = IdCuentaBeneficiaria,
        IdCategoria = IdCategoria,
    )

    transaccion.full_clean()
    transaccion.save()

    return transaccion

@transaction.atomic()
def ingreso_crear(
    usuario: User = None,
    Monto = None,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
) -> models.Transaccion:

    transaccion = transaccion_crear(
        usuario=usuario,
        Monto=Monto,
        Descripcion=Descripcion,
        Fecha=Fecha,
        IdCuentaBeneficiaria=IdCuentaOrdenante,
        IdPerfilBeneficiario=IdPerfilOrdenante,
        IdCategoria=IdCategoria,
    )

    return transaccion

@transaction.atomic()
def gasto_crear(
    usuario: User = None,
    Monto = None,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
) -> models.Transaccion:

    transaccion = transaccion_crear(
        usuario=usuario,
        Monto=Monto,
        Descripcion=Descripcion,
        Fecha=Fecha,
        IdCuentaOrdenante=IdCuentaOrdenante,
        IdPerfilOrdenante=IdPerfilOrdenante,
        IdCategoria=IdCategoria,
    )

    return transaccion

@transaction.atomic()
def transferencia_crear(
    usuario: User = None,
    Monto = None,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdPerfilBeneficiario: models.Perfil = None,
    IdCuentaBeneficiaria: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
    TransferenciaEntrePerfiles: bool = False,
) -> models.Transaccion:
    
    if TransferenciaEntrePerfiles is True:
        IdCuentaBeneficiaria = None
        IdCuentaOrdenante = None

    elif TransferenciaEntrePerfiles is False:
        IdPerfilBeneficiario = None
        IdPerfilOrdenante = None

    transaccion = transaccion_crear(
        usuario=usuario,
        Monto=Monto,
        Descripcion=Descripcion,
        Fecha=Fecha,
        IdCuentaOrdenante=IdCuentaOrdenante,
        IdCuentaBeneficiaria=IdCuentaBeneficiaria,
        IdPerfilOrdenante=IdPerfilOrdenante,
        IdPerfilBeneficiario=IdPerfilBeneficiario,
        IdCategoria=IdCategoria,
    )

    return transaccion
