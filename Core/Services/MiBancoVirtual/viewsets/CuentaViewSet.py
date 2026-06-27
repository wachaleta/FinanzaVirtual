from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import CuentaCrearValidator, CuentaEditarValidator
from ..models import *
from ..serializers import *

from Core.Services.MiBancoVirtual.Funciones import CuentaFunciones
from Core.Services.MiBancoVirtual import serializers

class CuentaViewSet(FinanzasModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        idUsuario = self.request.user.id

        cuentas = Cuenta.objects.filter(IdUsuario=idUsuario, Activo=True).order_by("Nombre")

        return cuentas
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        
        serializer.is_valid(raise_exception=True)

        cuenta = CuentaFunciones.cuenta_crear(
            usuario=request.user,
            **serializer.validated_data,
        ) 

        return Response({'id': cuenta.IdCuenta}, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        cuenta = self.get_object()

        serializer = serializers.CuentaEditarSerializer(data=request.data, context={'request': request}, instance=cuenta)
        serializer.is_valid(raise_exception=True)

        cuenta = CuentaFunciones.cuenta_editar(
            usuario=request.user,
            cuenta=cuenta,
            **serializer.validated_data,
        ) 

        return Response({'id': cuenta.IdCuenta}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        cuenta = self.get_object()

        cuenta = CuentaFunciones.cuenta_inactivar(
            usuario=request.user,
            cuenta=cuenta,
        )

        return Response({'id': cuenta.IdCuenta}, status=status.HTTP_200_OK)