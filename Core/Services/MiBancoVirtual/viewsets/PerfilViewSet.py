from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import PerfilCrearValidator, PerfilEditarValidator
from ..models import *
from ..serializers import *

from Core.Services.MiBancoVirtual.Funciones import PerfilFunciones

class PerfilViewSet(FinanzasModelViewSet):
    serializer_class = PerfilSerializer
    create_validator = PerfilCrearValidator
    update_validator = PerfilEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        searchText = self.request.query_params.get('searchText')

        idUsuario = self.request.user.id
        lista_perfiles = Perfil.objects.filter(IdUsuario = idUsuario, Activo=True)

        if searchText:
            lista_perfiles = lista_perfiles.filter(Nombre__icontains=searchText)

        perfiles = lista_perfiles.order_by('Nombre')
        
        return perfiles
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        perfil = PerfilFunciones.perfil_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': perfil.IdPerfil}, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        perfil = self.get_object()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        perfil = PerfilFunciones.perfil_editar(
            usuario=request.user,
            perfil=perfil,
            **serializer.validated_data,
        )

        return Response({'id': perfil.IdPerfil}, status=status.HTTP_200_OK)


    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        perfil = self.get_object()

        perfil = PerfilFunciones.perfil_inactivar(
            usuario=request.user,
            perfil=perfil,
        )

        return Response({'id': perfil.IdPerfil}, status=status.HTTP_200_OK)