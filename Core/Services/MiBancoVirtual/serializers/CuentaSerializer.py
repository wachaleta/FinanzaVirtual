from rest_framework import serializers
from ..models import *
from decimal import Decimal

class CuentaSerializer(serializers.ModelSerializer):
    saldo_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    saldo_mostrar = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta: 
        model = Cuenta
        fields = "__all__"
        read_only_fields = ("id", "usuario", "saldo_total")
    
    def create(self, validated_data):
        
        instance = Cuenta.objects.create(
            nombre = validated_data["nombre"],
            usuario = self.context["request"].user
        )

        return instance
