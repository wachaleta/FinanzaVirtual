from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from ..serializers import *

class TransaccionProgramadaPorIdViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionProgramadaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TransaccionProgramada.objects.filter(Id=self.kwargs["pk"])