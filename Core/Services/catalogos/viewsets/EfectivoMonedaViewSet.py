from rest_framework.permissions import IsAuthenticated

from Core.Application.Behaviours import FinanzasModelViewSet

from Core.Services.catalogos.getters import EfectivoMonedaGetters
from Core.Services.catalogos import serializers

class EfectivoMonedaViewSet(FinanzasModelViewSet):
    serializer_class = serializers.EfectivoMonedaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        efectivo_list = EfectivoMonedaGetters.obtener_efectivo_moneda_por_usuario(
            usuario=self.request.user
        )
        
        return efectivo_list