from rest_framework import serializers
from ..models import *

class GastoEditarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Transaccion
        fields = (
            "monto",
            "descripcion",
            "fecha",
            "perfil_ordenante",
            "cuenta_ordenante",
            "categoria",
        )
        read_only_fields = ("id",)