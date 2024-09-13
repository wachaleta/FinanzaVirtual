from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from ..serializers import *

class SubcuentaPorIdViewSet(viewsets.ModelViewSet):
    serializer_class = SubcuentaSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Subcuenta.objects.filter(id=self.kwargs["pk"])