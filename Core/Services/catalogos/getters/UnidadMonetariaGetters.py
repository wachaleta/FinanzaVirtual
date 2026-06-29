from django.db.transaction import atomic

from Core.Application.Exceptions import BadRequestException

from Core.Services.catalogos import models

@atomic()
def obtener_unidad_monetaria_por_id(
    id: int = None
) -> models.UnidadMonetaria:
    
    if not id:
        raise BadRequestException('No se proporcionó ningún id para encontrar la unidad monetaria')
    
    unidad_monetaria = models.UnidadMonetaria.objects.filter(id=id).first()

    return unidad_monetaria

@atomic()
def obtener_unidad_monetaria_por_simbolo(
    simbolo: str = None
) -> models.UnidadMonetaria:
    
    if not simbolo:
        raise BadRequestException('No se proporcionó ningún simbolo para encontrar la unidad monetaria')
    
    unidad_monetaria = models.UnidadMonetaria.objects.filter(simbolo=simbolo).first()

    return unidad_monetaria