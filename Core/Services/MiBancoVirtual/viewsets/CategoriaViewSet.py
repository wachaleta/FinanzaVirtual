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
        return Categoria.objects.filter(IdUsuario=self.request.user.id, Activo=True)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        categoria = CategoriaFunciones.categoria_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': categoria.IdCategoria}, status=status.HTTP_201_CREATED)


    def get_update_validated_data(self, data):
        return {
            "IdCategoria": data.get("IdCategoria", ""),
            "Nombre": data.get("Nombre", "")
        }
    
    def perform_destroy(self, instance):
        coincidencia = Transaccion.objects.filter(IdCategoria=instance.IdCategoria).exists()

        if coincidencia : 
            raise BadRequestException("No se puede eliminar la categoría porque ya existen transacciones que dependen de esta")
        return super().perform_destroy(instance)

    @action(methods=['put'], detail=True)
    def inactivar(self, request, pk=None):
        categoria = self.get_object()

        categoria.Activo = False

        categoria.save()

        return Response({
            'id': pk
        })