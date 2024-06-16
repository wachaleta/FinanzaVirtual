from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class PerfilCrearViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]

    def get_queryset(self):
        return Perfil.objects.filter(usuario=self.request.user.id).order_by("nombre")

