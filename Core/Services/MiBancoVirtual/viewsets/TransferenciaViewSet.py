from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransferenciaSerializer
from ..validators import TransferenciaCrearValidator

class TransferenciaViewSet(FinanzasModelViewSet):
    serializer_class = TransferenciaSerializer
    create_validator = TransferenciaCrearValidator()
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
        validated_data = {
            "Monto": data.get("Monto", 0),
            "Fecha": data.get("Fecha", ""),
            "IdCategoria": data.get("IdCategoria", ""),
            "Descripcion": data.get("Descripcion", ""),
            "TransferenciaEntrePerfiles": data.get("TransferenciaEntrePerfiles", ""),
        }
        print("ids")
        print(data.get("IdCategoria"))
        print(data.get("IdPerfilOrdenante"))
        if data.get("TransferenciaEntrePerfiles") == True:
            validated_data["IdPerfilOrdenante"] = data.get("IdPerfilOrdenante", "")
            validated_data["IdPerfilBeneficiario"] = data.get("IdPerfilBeneficiario", "")
        
        else:
            validated_data["IdCuentaOrdenante"] = data.get("IdCuentaOrdenante", "")
            validated_data["IdCuentaBeneficiaria"] = data.get("IdCuentaBeneficiaria", "")
            
        return  validated_data