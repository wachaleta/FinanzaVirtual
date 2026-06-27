from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransaccionSerializer

from Core.Services.MiBancoVirtual.Funciones import TransaccionFunciones

class TransaccionViewSet(FinanzasModelViewSet):
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        lista_transacciones = Transaccion.objects.filter(
                Q(IdPerfilOrdenante__IdUsuario = idUsuario) | Q(IdPerfilBeneficiario__IdUsuario = idUsuario) |
                Q(IdCuentaOrdenante__IdUsuario = idUsuario) | Q(IdCuentaBeneficiaria__IdUsuario = idUsuario) 
            )
        
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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     transaccion = TransaccionFunciones.transaccion_crear(
    #         usuario=request.user,
    #         **serializer.validated_data,
    #     )

    #     return Response({'id': transaccion.IdTransaccion}, status=status.HTTP_201_CREATED)
    def destroy(self, request, *args, **kwargs):
        transaccion = self.get_object()

        id = TransaccionFunciones.transaccion_eliminar(
            usuario=request.user,
            transaccion=transaccion,
        )

        return Response({'id': id}, status=status.HTTP_201_CREATED)