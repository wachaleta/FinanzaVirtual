from rest_framework import serializers
from ..models import *

class IngresoSerializer(serializers.ModelSerializer):
    
    nombre_subcuenta = serializers.CharField(source="subcuenta.nombre", read_only=True)
    nombre_categoria = serializers.CharField(source="categoria.nombre", read_only=True)
    class Meta: 
        model = Ingreso
        fields = "__all__"
        read_only_fields = ("id", "nombre_subcuenta", "nombre_categoria")

    def create(self, validated_data):
        instance = super().create(validated_data)

        instance.subcuenta.crear_ingreso(instance.monto)

        return instance
    
    def update(self, instance, validated_data):

        preSubcuenta = instance.subcuenta
        preMonto = instance.monto
        
        instance = super().update(instance, validated_data)

        if(preSubcuenta == instance.subcuenta):
            instance.subcuenta.crear_ingreso(instance.monto - preMonto)

        else:
            preSubcuenta.crear_gasto(preMonto)
            instance.subcuenta.crear_ingreso(instance.monto)

        return instance
