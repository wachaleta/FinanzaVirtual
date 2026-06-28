from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import CategoriaCrearValidator, CategoriaEditarValidator
from ..models import *
from ..serializers import *

from Core.Services.MiBancoVirtual.Funciones import CategoriaFunciones
class CategoriaViewSet(FinanzasModelViewSet):
    serializer_class = CategoriaSerializer
    create_validator = CategoriaCrearValidator
    update_validator = CategoriaEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter(usuario=self.request.user.id, activo=True)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request':request}
        )

        serializer.is_valid(raise_exception=True)

        categoria = CategoriaFunciones.categoria_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': categoria.id}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        categoria = self.get_object()

        serializer = self.serializer_class(
            data=request.data,
            context={'request':request},
            instance=categoria
        )

        serializer.is_valid(raise_exception=True)

        categoria = CategoriaFunciones.categoria_editar(
            usuario=request.user,
            categoria=categoria,
            **serializer.validated_data,
        )

        return Response({'id': categoria.id}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        categoria = self.get_object()

        categoria = CategoriaFunciones.categoria_inactivar(
            usuario=request.user,
            categoria=categoria,
        )

        return Response({'id': categoria.id}, status=status.HTTP_200_OK)