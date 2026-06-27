from datetime import date

from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

def transaccion_validar_inactivos(
    transaccion: models.Transaccion = None
):
    if transaccion.IdPerfilOrdenante and transaccion.IdPerfilOrdenante.Activo is False:
        raise BadRequestException("El perfil ordenante se encuentra inactivo")

    if transaccion.IdPerfilBeneficiario and transaccion.IdPerfilBeneficiario.Activo is False:
        raise BadRequestException("El perfil beneficiario se encuentra inactivo")

    if transaccion.IdCuentaOrdenante and transaccion.IdCuentaOrdenante.Activo is False:
        raise BadRequestException("La cuenta ordenante se encuentra inactiva")

    if transaccion.IdCuentaBeneficiaria and transaccion.IdCuentaBeneficiaria.Activo is False:
        raise BadRequestException("La cuenta beneficiaria se encuentra inactiva")

@transaction.atomic()
def transaccion_crear(
    usuario: User = None,
    Monto = 0,
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
def transaccion_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    Monto = 0,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdPerfilBeneficiario: models.Perfil = None,
    IdCuentaBeneficiaria: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
) -> models.Transaccion:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not transaccion:
        raise BadRequestException('No se proporcionó ninguna transacción para editar')
    
    transaccion_validar_inactivos(transaccion=transaccion)
    
    transaccion.Monto = Monto
    transaccion.Descripcion = Descripcion
    transaccion.Fecha = Fecha
    transaccion.IdPerfilOrdenante = IdPerfilOrdenante
    transaccion.IdCuentaOrdenante = IdCuentaOrdenante
    transaccion.IdPerfilBeneficiario = IdPerfilBeneficiario
    transaccion.IdCuentaBeneficiaria = IdCuentaBeneficiaria
    transaccion.IdCategoria = IdCategoria

    transaccion.full_clean()
    transaccion.save()

    return transaccion

@transaction.atomic()
def transaccion_eliminar(
    usuario: User = None,
    transaccion: models.Transaccion = None
):
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not transaccion:
        raise BadRequestException('No se proporcionó ninguna transacción para eliminar')

    transaccion_validar_inactivos(transaccion=transaccion)
    
    id = transaccion.IdTransaccion
    
    transaccion.delete()

    return id

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
def ingreso_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    Monto = None,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
) -> models.Transaccion:
    
    if not transaccion:
        raise BadRequestException('No se proporcionó ningún ingreso para editar')

    transaccion = transaccion_editar(
        usuario=usuario,
        transaccion=transaccion,
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
def gasto_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    Monto = None,
    Descripcion = None,
    Fecha: date = None,
    IdPerfilOrdenante: models.Perfil = None,
    IdCuentaOrdenante: models.Cuenta = None,
    IdCategoria: models.Categoria = None,
) -> models.Transaccion:
    
    if not transaccion:
        raise BadRequestException('No se proporcionó nignún gasto para editar')

    transaccion = transaccion_editar(
        usuario=usuario,
        transaccion=transaccion,
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

@transaction.atomic()
def transferencia_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
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
    
    if not transaccion:
        raise BadRequestException('No se proporcionó ninguna transferencia para editar')
    
    if TransferenciaEntrePerfiles is True:
        IdCuentaBeneficiaria = None
        IdCuentaOrdenante = None

    elif TransferenciaEntrePerfiles is False:
        IdPerfilBeneficiario = None
        IdPerfilOrdenante = None

    transaccion = transaccion_editar(
        usuario=usuario,
        transaccion=transaccion,
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
