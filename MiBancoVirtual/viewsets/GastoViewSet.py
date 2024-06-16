from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *

class GastoViewSet(viewsets.ModelViewSet):
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        subcuenta_param = self.request.query_params.get("subcuenta")

        lista_categorias = list(map(lambda x: x.id, Categoria.objects.filter(usuario=self.request.user.id)))
        lista_gastos = Gasto.objects.filter(categoria__in = lista_categorias)

        if(subcuenta_param):
            lista_gastos = lista_gastos.filter(subcuenta=subcuenta_param)

        return lista_gastos
