from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *
    
class IngresoViewSet(viewsets.ModelViewSet):
    
    serializer_class = IngresoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        lista_categorias = list(map(lambda x: x.id, Categoria.objects.filter(usuario=self.request.user.id)))
        lista_ingresos = Ingreso.objects.filter(categoria__in = lista_categorias)

        return lista_ingresos
