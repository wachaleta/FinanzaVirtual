from rest_framework import serializers
from ..models import *

class GastoSerializer(serializers.ModelSerializer):
    nombre_subcuenta = serializers.CharField(source="subcuenta.nombre", read_only=True)
    nombre_categoria = serializers.CharField(source="categoria.nombre", read_only=True)
    class Meta: 
        model = Gasto
        fields = "__all__"
        read_only_fields = ("id", "nombre_subcuenta", "nombre_categoria")

    def create(self, validated_data):
        instance= super().create(validated_data)

        instance.subcuenta.crear_gasto(instance.monto)

        return instance

    def update(self, instance, validated_data):

        preMonto = instance.monto
        preSubcuenta = instance.subcuenta

        super().update(instance, validated_data)

        if(preSubcuenta == instance.subcuenta):
            
            instance.subcuenta.crear_gasto(instance.monto - preMonto)
        
        else:
            preSubcuenta.crear_ingreso(preMonto)
            instance.subcuenta.crear_gasto(instance.monto)

        return instance
