from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Coalesce
from django.db.models import Sum, Subquery, OuterRef, Value, DecimalField, Q, Case, When

from django.db import connection
from ..models import *
from ..serializers import *

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):

        idUsuario = self.request.user.id
        lista_perfiles = Perfil.objects.filter(usuario = idUsuario)

        perfiles = lista_perfiles.order_by('-agregarTotal', 'nombre')
        
        print(connection.queries)
        return perfiles