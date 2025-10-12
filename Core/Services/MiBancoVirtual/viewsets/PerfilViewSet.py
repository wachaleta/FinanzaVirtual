from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ....Application.Behaviours import FinanzasModelViewSet
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
        lista_perfiles = Perfil.objects.filter(IdUsuario = idUsuario)

        perfiles = lista_perfiles.order_by('Nombre')
        
        return perfiles
    
    def get_create_validated_data(self, data):
        return {
            "Nombre": data.get("Nombre", ""),
            "AgregarTotal": data.get("AgregarTotal", False)
        }
    
    def get_update_validated_data(self, data):
        return {
            "IdPerfil": data["IdPerfil"],
            "Nombre": data.get("Nombre", ""),
            "AgregarTotal": data.get("AgregarTotal", False)
        }