from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransferenciaSerializer
from ..validators import TransferenciaCrearValidator, TransferenciaEditarValidator

from Core.Services.MiBancoVirtual.Funciones import TransaccionFunciones
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
        
        return lista_transacciones.order_by("-Fecha", "-FechaCreacion")
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaccion = TransaccionFunciones.transferencia_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': transaccion.IdTransaccion}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        transaccion = self.get_object()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaccion = TransaccionFunciones.transferencia_editar(
            usuario=request.user,
            transaccion=transaccion,
            **serializer.validated_data,
        )

        return Response({'id': transaccion.IdTransaccion}, status=status.HTTP_201_CREATED)