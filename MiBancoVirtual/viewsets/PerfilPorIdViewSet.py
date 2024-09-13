from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from ..serializers import *

class PerfilPorIdViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Perfil.objects.filter(id=self.kwargs["pk"])