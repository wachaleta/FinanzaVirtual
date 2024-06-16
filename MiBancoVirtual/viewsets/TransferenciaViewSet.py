from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *
    
class TransferenciaViewSet(viewsets.ModelViewSet):
    
    serializer_class = TransferenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lista_cuentas = list(map(lambda x: x.id, Cuenta.objects.filter(usuario=self.request.user.id)))
        lista_subcuentas = list(map(lambda x: x.id, Subcuenta.objects.filter(cuenta__in=lista_cuentas)))
        lista_transferencias = Transferencia.objects.filter(ordenante__in = lista_subcuentas)
        
        return lista_transferencias