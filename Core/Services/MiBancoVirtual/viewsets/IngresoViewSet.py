from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import IngresoSerializer
from ..validators import IngresoCrearValidator

class IngresoViewSet(FinanzasModelViewSet):
    serializer_class = IngresoSerializer
    create_validator = IngresoCrearValidator()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id
        # fechaInicio = self.request.query_params.get("fechaInicio")
        # fechaFinal = self.request.query_params.get("fechaFinal")

        lista_transacciones = Transaccion.objects.filter(
                Q(IdPerfilOrdenante__IdUsuario = idUsuario) | Q(IdPerfilBeneficiario__IdUsuario = idUsuario) |
                Q(IdCuentaOrdenante__IdUsuario = idUsuario) | Q(IdCuentaBeneficiaria__IdUsuario = idUsuario) 
            )
        # .filter(fecha__gte = fechaInicio).filter(fecha__lte = fechaFinal)
        
        return lista_transacciones.annotate(
            ordenante_nombre = Concat(
                F("IdCuentaOrdenante__Nombre"), 
                Value(" - "),
                F("IdPerfilOrdenante__Nombre")
            )
        ).annotate(
            beneficiario_nombre = Concat(
                F("IdCuentaBeneficiaria__Nombre"), 
                Value(" - "),
                F("IdPerfilBeneficiario__Nombre")
            )
        ).order_by("-Fecha").order_by("-FechaCreacion")
    
    def get_create_validated_data(self, data):
        return {
            "Monto": data.get("Monto", 0),
            "Fecha": data.get("Fecha", ""),
            "IdCuentaBeneficiaria": data.get("IdCuentaOrdenante", ""),
            "IdPerfilBeneficiario": data.get("IdPerfilOrdenante", ""),
            "IdCategoria": data.get("IdCategoria", ""),
            "Descripcion": data.get("Descripcion", ""),
        }