from rest_framework import serializers
from ..models import *

class IngresoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        validated_data["IdPerfilOrdenante"] = None
        validated_data["IdCuentaOrdenante"] = None
        return super().update(instance, validated_data)