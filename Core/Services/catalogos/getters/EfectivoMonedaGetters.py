from Core.Services.Auth.getters import ProfileGetters

from Core.Services.catalogos import models
from Core.Services.catalogos.getters import UnidadMonetariaGetters

def obtener_efectivo_moneda_por_usuario(
    usuario = None
):
    profile = ProfileGetters.obtener_profile_por_usuario(usuario=usuario)

    unidad_monetaria = UnidadMonetariaGetters.obtener_unidad_monetaria_por_id(id=profile.unidad_monetaria.id)
    
    efectivo_list = models.EfectivoMoneda.objects.filter(
        unidad_monetaria=unidad_monetaria
    ).order_by('-valor')

    return efectivo_list

def obtener_efectivo_moneda_por_id(
    id = None
):

    efectivo_moneda = models.EfectivoMoneda.objects.filter(id=id).first()

    return efectivo_moneda