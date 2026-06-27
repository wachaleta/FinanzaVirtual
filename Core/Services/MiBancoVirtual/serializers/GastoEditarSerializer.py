from rest_framework import serializers
from ..models import *

class GastoEditarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Transaccion
        fields = (
            "Monto",
            "Descripcion",
            "Fecha",
            "IdPerfilOrdenante",
            "IdCuentaOrdenante",
            "IdCategoria",
        )
        read_only_fields = ("id",)