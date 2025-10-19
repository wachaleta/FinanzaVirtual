from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import PerfilCrearValidator, PerfilEditarValidator
from ..models import *
from ..serializers import *

class PerfilViewSet(FinanzasModelViewSet):
    serializer_class = PerfilSerializer
    create_validator = PerfilCrearValidator
    update_validator = PerfilEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        idUsuario = self.request.user.id
        lista_perfiles = Perfil.objects.filter(IdUsuario = idUsuario, Activo=True)

        perfiles = lista_perfiles.order_by('Nombre')
        
        return perfiles
    
    def get_create_validated_data(self, data):
        return {
            "Nombre": data.get("Nombre", ""),
            "SumaDisponible": data.get("SumaDisponible", False)
        }
    
    def get_update_validated_data(self, data):
        return {
            "IdPerfil": data["IdPerfil"],
            "Nombre": data.get("Nombre", ""),
            "SumaDisponible": data.get("SumaDisponible", False)
        }

    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        perfil = self.get_object()

        if(perfil.Saldo != 0):
            raise BadRequestException("Este perfil aún tiene saldo")

        perfil.Activo = False

        perfil.save()

        return Response({
            'id': pk
        })