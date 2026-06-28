from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import PerfilCrearValidator, PerfilEditarValidator
from ..models import *

from Core.Services.MiBancoVirtual.getters import PerfilGetters
from Core.Services.MiBancoVirtual.Funciones import PerfilFunciones
from Core.Services.MiBancoVirtual import serializers

class PerfilViewSet(FinanzasModelViewSet):
    serializer_class = serializers.PerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        serializer = serializers.PerfilesListSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        perfiles = PerfilGetters.obtener_perfiles_usuario(
            usuario=self.request.user,
            **serializer.validated_data
        )
        
        return perfiles
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        
        perfil = PerfilFunciones.perfil_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': perfil.id}, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        perfil = self.get_object()

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request},
            instance=perfil,
        )

        serializer.is_valid(raise_exception=True)
        
        perfil = PerfilFunciones.perfil_editar(
            usuario=request.user,
            perfil=perfil,
            **serializer.validated_data,
        )

        return Response({'id': perfil.id}, status=status.HTTP_200_OK)


    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        perfil = self.get_object()

        perfil = PerfilFunciones.perfil_inactivar(
            usuario=request.user,
            perfil=perfil,
        )

        return Response({'id': perfil.id}, status=status.HTTP_200_OK)