from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ....Application.Behaviours import FinanzasModelViewSet
from ....Application.Exceptions import BadRequestException
from ..validators import CategoriaCrearValidator, CategoriaEditarValidator
from ..models import *
from ..serializers import *

class CategoriaViewSet(FinanzasModelViewSet):
    serializer_class = CategoriaSerializer
    create_validator = CategoriaCrearValidator
    update_validator = CategoriaEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter(IdUsuario=self.request.user.id)

    def get_create_validated_data(self, data):
        return {
            "Nombre": data.get("Nombre", "")
        }

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