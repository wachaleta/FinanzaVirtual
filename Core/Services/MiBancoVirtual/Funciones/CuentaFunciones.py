from django.contrib.auth.models import User
from django.db import transaction  

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
):
    cuenta = models.Cuenta(
        IdUsuario = usuario,
        Nombre = nombre,
        EsEfectivo = es_efectivo,
        SaldoReal = saldo_real,
        BQ100 = bQ100,
        BQ50 = bQ50,
        BQ20 = bQ20,
        BQ10 = bQ10,
        BQ5 = bQ5,
        M100c = m100c,
        M50c = m50c,
        M25c = m25c,
        M10c = m10c,
        M5c = m5c,
    )

    cuenta.full_clean()
    cuenta.save()

    return cuenta