from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class TransaccionCrearViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionCrearSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaccion.objects.all()