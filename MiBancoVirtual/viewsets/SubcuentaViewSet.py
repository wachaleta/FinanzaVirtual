from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *

class SubcuentaViewSet(viewsets.ModelViewSet):
    serializer_class = SubcuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #   Obtiene todos los ids de las cuentas que pertenezcan al usuario logueado
        lista_cuentas = list(map(lambda x: x.id, Cuenta.objects.filter(usuario=self.request.user.id)))  
        lista_subcuentas = Subcuenta.objects.filter(cuenta__in = lista_cuentas)

        return lista_subcuentas.order_by("nombre")
