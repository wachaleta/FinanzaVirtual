from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import GastoSerializer, GastoEditarSerializer
from ..validators import GastoCrearValidator, GastoEditarValidator

from Core.Services.MiBancoVirtual.Funciones import TransaccionFunciones
class GastoViewSet(FinanzasModelViewSet):
    serializer_class = GastoSerializer
    create_validator = GastoCrearValidator
    update_validator = GastoEditarValidator
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
        ).order_by("-Fecha", "-FechaCreacion")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaccion = TransaccionFunciones.gasto_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': transaccion.IdTransaccion}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        transaccion = self.get_object()

        serializer = GastoEditarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaccion = TransaccionFunciones.gasto_editar(
            usuario=request.user,
            transaccion=transaccion,
            **serializer.validated_data,
        )

        return Response({'id': transaccion.IdTransaccion}, status=status.HTTP_200_OK)