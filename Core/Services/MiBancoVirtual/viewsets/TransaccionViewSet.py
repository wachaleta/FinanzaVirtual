from rest_framework import viewsets
from django.db.models import Q,  OuterRef, Value, F, Subquery, CharField
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class TransaccionViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionCrearSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id
        fechaInicio = self.request.query_params.get("fechaInicio")
        fechaFinal = self.request.query_params.get("fechaFinal")

        lista_transacciones = Transaccion.objects.filter(
                Q(perfilOrdenante__usuario = idUsuario) | Q(perfilBeneficiario__usuario = idUsuario) |
                Q(cuentaOrdenante__usuario = idUsuario) | Q(cuentaBeneficiaria__usuario = idUsuario) 
            ).filter(fecha__gte = fechaInicio).filter(fecha__lte = fechaFinal)
        
        return lista_transacciones.annotate(
            ordenante_nombre = Concat(
                F("cuentaOrdenante__nombre"), 
                Value(" - "),
                F("perfilOrdenante__nombre")
            )
        ).annotate(
            beneficiario_nombre = Concat(
                F("cuentaBeneficiaria__nombre"), 
                Value(" - "),
                F("perfilBeneficiario__nombre")
            )
        ).order_by("-fecha").order_by("-fechaCreacion")