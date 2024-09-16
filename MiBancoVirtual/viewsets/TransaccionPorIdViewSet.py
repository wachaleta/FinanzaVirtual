from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from ..serializers import *

class TransaccionPorIdViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionPorIdSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Transaccion.objects.filter(id=self.kwargs["pk"])