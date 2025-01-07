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

        perfiles = lista_perfiles.annotate(
            saldo = 
                Coalesce(
                    Subquery(
                        Transaccion.objects.filter(
                            beneficiario__perfil_id__in=OuterRef("id")
                        ).values("beneficiario__perfil").annotate(
                            total=Sum('monto', default=0)  
                        ).values('total'),
                        default=0,
                        output_field=DecimalField(default=0)
                    ),
                    Value(0, DecimalField())
                )
                -
                Coalesce(
                    Subquery(
                        Transaccion.objects.filter(
                            ordenante__perfil_id__in=OuterRef("id")
                        ).values("ordenante__perfil").annotate(
                            total=Sum('monto', default=0)  
                        ).values('total'),
                        default=0,
                        output_field=DecimalField(default=0)
                    ),
                    Value(0, DecimalField())
                )
        ).order_by('nombre')
        
        print(connection.queries)
        return perfiles