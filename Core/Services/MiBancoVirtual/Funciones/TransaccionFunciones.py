from datetime import date

from django.contrib.auth.models import User
from django.db import transaction  

from Core.Application.Exceptions import BadRequestException
from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

def transaccion_validar_inactivos(
    transaccion: models.Transaccion = None
):
    if transaccion.perfil_ordenante and transaccion.perfil_ordenante.activo is False:
        raise BadRequestException("El perfil ordenante se encuentra inactivo")

    if transaccion.perfil_beneficiario and transaccion.perfil_beneficiario.activo is False:
        raise BadRequestException("El perfil beneficiario se encuentra inactivo")

    if transaccion.cuenta_ordenante and transaccion.cuenta_ordenante.activo is False:
        raise BadRequestException("La cuenta ordenante se encuentra inactiva")

    if transaccion.cuenta_beneficiaria and transaccion.cuenta_beneficiaria.activo is False:
        raise BadRequestException("La cuenta beneficiaria se encuentra inactiva")

@transaction.atomic()
def transaccion_crear(
    usuario: User = None,
    monto = 0,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    perfil_beneficiario: models.Perfil = None,
    cuenta_beneficiaria: models.Cuenta = None,
    categoria: models.Categoria = None,
) -> models.Transaccion:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    transaccion = models.Transaccion(
        monto = monto,
        descripcion = descripcion,
        fecha = fecha,
        perfil_ordenante = perfil_ordenante,
        cuenta_ordenante = cuenta_ordenante,
        perfil_beneficiario = perfil_beneficiario,
        cuenta_beneficiaria = cuenta_beneficiaria,
        categoria = categoria,
    )

    transaccion_validar_inactivos(transaccion=transaccion)

    transaccion.full_clean()
    transaccion.save()

    return transaccion

@transaction.atomic()
def transaccion_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    monto = 0,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    perfil_beneficiario: models.Perfil = None,
    cuenta_beneficiaria: models.Cuenta = None,
    categoria: models.Categoria = None,
) -> models.Transaccion:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    if not transaccion:
        raise BadRequestException('No se proporcionó ninguna transacción para editar')
    
    transaccion_validar_inactivos(transaccion=transaccion)
    
    transaccion.monto = monto
    transaccion.descripcion = descripcion
    transaccion.fecha = fecha
    transaccion.perfil_ordenante = perfil_ordenante
    transaccion.cuenta_ordenante = cuenta_ordenante
    transaccion.perfil_beneficiario = perfil_beneficiario
    transaccion.cuenta_beneficiaria = cuenta_beneficiaria
    transaccion.categoria = categoria

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
    
    id = transaccion.id
    
    transaccion.delete()

    return id

@transaction.atomic()
def ingreso_crear(
    usuario: User = None,
    monto = None,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    categoria: models.Categoria = None,
) -> models.Transaccion:

    transaccion = transaccion_crear(
        usuario=usuario,
        monto=monto,
        descripcion=descripcion,
        fecha=fecha,
        cuenta_beneficiaria=cuenta_ordenante,
        perfil_beneficiario=perfil_ordenante,
        categoria=categoria,
    )

    return transaccion

@transaction.atomic()
def ingreso_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    monto = None,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    categoria: models.Categoria = None,
) -> models.Transaccion:
    
    if not transaccion:
        raise BadRequestException('No se proporcionó ningún ingreso para editar')

    transaccion = transaccion_editar(
        usuario=usuario,
        transaccion=transaccion,
        monto=monto,
        descripcion=descripcion,
        fecha=fecha,
        cuenta_beneficiaria=cuenta_ordenante,
        perfil_beneficiario=perfil_ordenante,
        categoria=categoria,
    )

    return transaccion

@transaction.atomic()
def gasto_crear(
    usuario: User = None,
    monto = None,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    categoria: models.Categoria = None,
) -> models.Transaccion:

    transaccion = transaccion_crear(
        usuario=usuario,
        monto=monto,
        descripcion=descripcion,
        fecha=fecha,
        cuenta_ordenante=cuenta_ordenante,
        perfil_ordenante=perfil_ordenante,
        categoria=categoria,
    )

    return transaccion

@transaction.atomic()
def gasto_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    monto = None,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    categoria: models.Categoria = None,
) -> models.Transaccion:
    
    if not transaccion:
        raise BadRequestException('No se proporcionó nignún gasto para editar')

    transaccion = transaccion_editar(
        usuario=usuario,
        transaccion=transaccion,
        monto=monto,
        descripcion=descripcion,
        fecha=fecha,
        cuenta_ordenante=cuenta_ordenante,
        perfil_ordenante=perfil_ordenante,
        categoria=categoria,
    )

    return transaccion

@transaction.atomic()
def transferencia_crear(
    usuario: User = None,
    monto = None,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    perfil_beneficiario: models.Perfil = None,
    cuenta_beneficiaria: models.Cuenta = None,
    categoria: models.Categoria = None,
    transferencia_entre_perfiles: bool = False,
) -> models.Transaccion:
    
    if transferencia_entre_perfiles is True:
        cuenta_beneficiaria = None
        cuenta_ordenante = None

    elif transferencia_entre_perfiles is False:
        perfil_beneficiario = None
        perfil_ordenante = None

    transaccion = transaccion_crear(
        usuario=usuario,
        monto=monto,
        descripcion=descripcion,
        fecha=fecha,
        cuenta_ordenante=cuenta_ordenante,
        cuenta_beneficiaria=cuenta_beneficiaria,
        perfil_ordenante=perfil_ordenante,
        perfil_beneficiario=perfil_beneficiario,
        categoria=categoria,
    )

    return transaccion

@transaction.atomic()
def transferencia_editar(
    usuario: User = None,
    transaccion: models.Transaccion = None,
    monto = None,
    descripcion = None,
    fecha: date = None,
    perfil_ordenante: models.Perfil = None,
    cuenta_ordenante: models.Cuenta = None,
    perfil_beneficiario: models.Perfil = None,
    cuenta_beneficiaria: models.Cuenta = None,
    categoria: models.Categoria = None,
    transferencia_entre_perfiles: bool = False,
) -> models.Transaccion:
    
    if not transaccion:
        raise BadRequestException('No se proporcionó ninguna transferencia para editar')
    
    if transferencia_entre_perfiles is True:
        cuenta_beneficiaria = None
        cuenta_ordenante = None

    elif transferencia_entre_perfiles is False:
        perfil_beneficiario = None
        perfil_ordenante = None

    transaccion = transaccion_editar(
        usuario=usuario,
        transaccion=transaccion,
        monto=monto,
        descripcion=descripcion,
        fecha=fecha,
        cuenta_ordenante=cuenta_ordenante,
        cuenta_beneficiaria=cuenta_beneficiaria,
        perfil_ordenante=perfil_ordenante,
        perfil_beneficiario=perfil_beneficiario,
        categoria=categoria,
    )

    return transaccion
