from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):

        idUsuario = self.request.user.id
        lista_perfiles = Perfil.objects.filter(IdUsuario = idUsuario)

        perfiles = lista_perfiles.order_by('-AgregarTotal', 'Nombre')
        
        return perfiles