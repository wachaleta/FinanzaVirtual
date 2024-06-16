from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cuenta.objects.filter(usuario=self.request.user.id).order_by("nombre")
