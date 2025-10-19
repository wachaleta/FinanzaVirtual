from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import CuentaCrearValidator, CuentaEditarValidator
from ..models import *
from ..serializers import *

class CuentaViewSet(FinanzasModelViewSet):
    serializer_class = CuentaSerializer
    create_validator = CuentaCrearValidator
    update_validator = CuentaEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        idUsuario = self.request.user.id

        cuentas = Cuenta.objects.filter(IdUsuario=idUsuario, Activo=True).order_by("Nombre")

        return cuentas
    
    def get_create_validated_data(self, data):
        return {
            "Nombre": data.get("Nombre", ""),
            "EsEfectivo": data.get("EsEfectivo", False),
            "SaldoReal": data.get("SaldoReal", 0),
            "BQ100": data.get("BQ100", 0),
            "BQ50": data.get("BQ50", 0),
            "BQ20": data.get("BQ20", 0),
            "BQ10": data.get("BQ10", 0),
            "BQ5": data.get("BQ5", 0),
            "M100c": data.get("M100c", 0),
            "M50c": data.get("M50c", 0),
            "M25c": data.get("M25c", 0),
            "M10c": data.get("M10c", 0),
            "M5c": data.get("M5c", 0),
        }
    
    def get_update_validated_data(self, data):
        return {
            "IdCuenta": data["IdCuenta"],
            "Nombre": data.get("Nombre", ""),
            "EsEfectivo": data.get("EsEfectivo", False),
            "SaldoReal": data.get("SaldoReal", 0),
            "BQ100": data.get("BQ100", 0),
            "BQ50": data.get("BQ50", 0),
            "BQ20": data.get("BQ20", 0),
            "BQ10": data.get("BQ10", 0),
            "BQ5": data.get("BQ5", 0),
            "M100c": data.get("M100c", 0),
            "M50c": data.get("M50c", 0),
            "M25c": data.get("M25c", 0),
            "M10c": data.get("M10c", 0),
            "M5c": data.get("M5c", 0),
        }

    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        cuenta = self.get_object()

        if(cuenta.SaldoTotal != 0):
            raise BadRequestException("Esta cuenta aún tiene saldo")

        cuenta.Activo = False

        cuenta.save()

        return Response({
            'id': pk
        })