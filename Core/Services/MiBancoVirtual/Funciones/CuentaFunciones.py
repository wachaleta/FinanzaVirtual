from django.contrib.auth.models import User
from django.db import transaction  

from Core.Services.Auth.Funciones import ProfileFunciones
from Core.Services.MiBancoVirtual import models

@transaction.atomic()
def cuenta_crear(
    usuario: User = None,
    Nombre: str = None,
    EsEfectivo: bool = False,
    SaldoReal: int = 0,
    BQ100: int = 0,
    BQ50: int = 0,
    BQ20: int = 0,
    BQ10: int = 0,
    BQ5: int = 0,
    M100c: int = 0,
    M50c: int = 0,
    M25c: int = 0,
    M10c: int = 0,
    M5c: int = 0,
) -> models.Cuenta:
    ProfileFunciones.profile_validar_pago(usuario=usuario)

    cuenta = models.Cuenta(
        IdUsuario = usuario,
        Nombre = Nombre,
        EsEfectivo = EsEfectivo,
        SaldoReal = SaldoReal,
        BQ100 = BQ100,
        BQ50 = BQ50,
        BQ20 = BQ20,
        BQ10 = BQ10,
        BQ5 = BQ5,
        M100c = M100c,
        M50c = M50c,
        M25c = M25c,
        M10c = M10c,
        M5c = M5c,
    )

    cuenta.full_clean()
    cuenta.save()

    return cuenta