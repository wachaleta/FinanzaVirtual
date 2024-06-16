from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Perfil.objects.filter(usuario=self.request.user.id).order_by("nombre")

