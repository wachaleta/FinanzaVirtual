from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from ..serializers import *

class TransaccionProgramadaDetallePorIdViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionProgramadaDetalleSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TransaccionProgramadaDetalle.objects.filter(Id=self.kwargs["pk"])