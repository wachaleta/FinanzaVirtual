from rest_framework import serializers
from ..models import *

class TransaccionSerializer(serializers.ModelSerializer):
    TransferenciaEntrePerfiles = serializers.BooleanField(read_only=True)

    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        validated_data["IdPerfilBeneficiario"] = None
        validated_data["IdCuentaBeneficiaria"] = None
        return super().update(instance, validated_data)