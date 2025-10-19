from django.db.models import Q

from rest_framework.permissions import IsAuthenticated

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransferenciaSerializer
from ..validators import TransferenciaCrearValidator, TransferenciaEditarValidator

class TransferenciaViewSet(FinanzasModelViewSet):
    serializer_class = TransferenciaSerializer
    create_validator = TransferenciaCrearValidator
    update_validator = TransferenciaEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        lista_transacciones = Transaccion.objects.filter(
                Q(IdPerfilOrdenante__IdUsuario = idUsuario) | Q(IdPerfilBeneficiario__IdUsuario = idUsuario) |
                Q(IdCuentaOrdenante__IdUsuario = idUsuario) | Q(IdCuentaBeneficiaria__IdUsuario = idUsuario) 
            )
        
        return lista_transacciones.order_by("-Fecha").order_by("-FechaCreacion")
    
    def get_create_validated_data(self, data):
        validated_data = {
            "Monto": data.get("Monto", 0),
            "Fecha": data.get("Fecha", ""),
            "IdCategoria": data.get("IdCategoria", ""),
            "Descripcion": data.get("Descripcion", ""),
            "TransferenciaEntrePerfiles": data.get("TransferenciaEntrePerfiles", ""),
        }

        if data.get("TransferenciaEntrePerfiles") == True:
            validated_data["IdPerfilOrdenante"] = data.get("IdPerfilOrdenante", "")
            validated_data["IdPerfilBeneficiario"] = data.get("IdPerfilBeneficiario", "")
        
        else:
            validated_data["IdCuentaOrdenante"] = data.get("IdCuentaOrdenante", "")
            validated_data["IdCuentaBeneficiaria"] = data.get("IdCuentaBeneficiaria", "")
            
        return  validated_data
    
    def get_update_validated_data(self, data):
        validated_data = {
            "IdTransaccion": data.get("IdTransaccion"),
            "Monto": data.get("Monto", 0),
            "Fecha": data.get("Fecha", ""),
            "IdCategoria": data.get("IdCategoria", ""),
            "Descripcion": data.get("Descripcion", ""),
            "TransferenciaEntrePerfiles": data.get("TransferenciaEntrePerfiles", ""),
        }
        

        if data.get("TransferenciaEntrePerfiles") == True:
            validated_data["IdPerfilOrdenante"] = data.get("IdPerfilOrdenante", "")
            validated_data["IdPerfilBeneficiario"] = data.get("IdPerfilBeneficiario", "")
        
        else:
            validated_data["IdCuentaOrdenante"] = data.get("IdCuentaOrdenante", "")
            validated_data["IdCuentaBeneficiaria"] = data.get("IdCuentaBeneficiaria", "")
            
        return  validated_data