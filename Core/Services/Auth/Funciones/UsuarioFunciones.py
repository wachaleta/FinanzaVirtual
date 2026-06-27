from django.contrib.auth.models import User
from django.db import transaction

from Core.Services.Auth.Funciones import ProfileFunciones

from Core.Services.MiBancoVirtual.Funciones import CategoriaFunciones, PerfilFunciones, CuentaFunciones

@transaction.atomic()
def usuario_crear(
    username: str = None,
    password: str = None,
    password_again: str = None,
):
    usuario = User.objects.create_user(
        username=username,
        password=password
    )

    usuario.save()

    ProfileFunciones.profile_crear(usuario=usuario)

    CategoriaFunciones.categoria_crear(
        usuario=usuario,
        nombre="Otros"
    )

    CategoriaFunciones.categoria_crear(
        usuario=usuario,
        nombre="Comida"
    )

    CategoriaFunciones.categoria_crear(
        usuario=usuario,
        nombre="Casa"
    )

    CategoriaFunciones.categoria_crear(
        usuario=usuario,
        nombre="Ropa"
    )

    PerfilFunciones.perfil_crear(
        usuario=usuario,
        nombre=usuario.username
    )

    CuentaFunciones.cuenta_crear(
        usuario=usuario,
        nombre="Billetera",
        es_efectivo=True
    )

    CuentaFunciones.cuenta_crear(
        usuario=usuario,
        nombre="Banco",
        es_efectivo=False
    )

    return usuario