from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import CuentaCrearValidator, CuentaEditarValidator
from ..models import *

from Core.Services.MiBancoVirtual.getters import CuentaGetters
from Core.Services.MiBancoVirtual.Funciones import CuentaFunciones
from Core.Services.MiBancoVirtual import serializers

class CuentaViewSet(FinanzasModelViewSet):
    serializer_class = serializers.CuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        serializer = serializers.CuentasListRequestSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        cuentas = CuentaGetters.obtener_cuentas_usuario(
            usuario=self.request.user,
            **serializer.validated_data
        )
        
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

        return Response({'id': cuenta.id}, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        cuenta = self.get_object()

        serializer = serializers.CuentaEditarSerializer(data=request.data, context={'request': request}, instance=cuenta)
        serializer.is_valid(raise_exception=True)

        cuenta = CuentaFunciones.cuenta_editar(
            usuario=request.user,
            cuenta=cuenta,
            **serializer.validated_data,
        ) 

        return Response({'id': cuenta.id}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        cuenta = self.get_object()

        CuentaFunciones.cuenta_inactivar(
            usuario=request.user,
            cuenta=cuenta,
        )

        return Response({'id': cuenta.id}, status=status.HTTP_200_OK)