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
                Q(ordenante__perfil__usuario = idUsuario) | Q(beneficiario__perfil__usuario = idUsuario)
            ).filter(fecha__gte = fechaInicio).filter(fecha__lte = fechaFinal).order_by("-fecha")
        
        return lista_transacciones.annotate(
            ordenante_nombre = Concat(
                        F("ordenante__cuenta__nombre"), 
                        Value(" - "),
                        F("ordenante__perfil__nombre")
                    )
        ).annotate(
            beneficiario_nombre = Concat(
                        F("beneficiario__cuenta__nombre"), 
                        Value(" - "),
                        F("beneficiario__perfil__nombre")
                    )
        )