from rest_framework import serializers
from ..models import *

class CuentaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cuenta
        fields = "__all__"
        read_only_fields = ("id", "saldo_total", "usuario",)

    def create(self, validated_data):
        
        instance = Cuenta.objects.create(
            nombre = validated_data["nombre"],
            usuario = self.context["request"].user
        )

        return instance
    
    def update(self, instance, validated_data):

        super().update(instance, validated_data)
        
        lista_subcuentas = Subcuenta.objects.filter(cuenta=instance.id)

        for subcuenta in lista_subcuentas:
            
            subcuenta.cambiar_nombre()
            subcuenta.save()

        return instance
