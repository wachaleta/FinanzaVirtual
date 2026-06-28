from rest_framework import serializers
from ..models import *

class TransaccionSerializer(serializers.ModelSerializer):
    transferencia_entre_perfiles = serializers.BooleanField(read_only=True)

    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        validated_data["perfil_beneficiario"] = None
        validated_data["cuenta_beneficiaria"] = None
        return super().update(instance, validated_data)