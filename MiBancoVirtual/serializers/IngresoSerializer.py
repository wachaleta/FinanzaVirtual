from rest_framework import serializers
from ..models import *

class IngresoSerializer(serializers.ModelSerializer):
    subcuenta = serializers.IntegerField()
    subcuenta_nombre = serializers.CharField()
    categoria_nombre = serializers.CharField()

    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id", "subcuenta_nombre", "categoria_nombre", "subcuenta")

    def create(self, validated_data):
        instance = super().create(validated_data)

        instance.subcuenta.crear_ingreso(instance.monto)

        return instance
    
    def update(self, instance, validated_data):
        
        #   Revierte el ingreso anterior
        instance.subcuenta.crear_gasto(instance.monto)

        #   Modifica el ingreso
        instance = super().update(instance, validated_data)

        #   Crea el nuevo ingreso
        subcuenta = Subcuenta.objects.filter(id=instance.subcuenta.id).first()

        subcuenta.crear_ingreso(instance.monto)

        return instance
