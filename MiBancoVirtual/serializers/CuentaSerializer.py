from rest_framework import serializers
from ..models import *
from decimal import Decimal

class CuentaSerializer(serializers.ModelSerializer):
    total_efectivo = serializers.SerializerMethodField()
    diferencia_efectivo = serializers.SerializerMethodField()

    class Meta: 
        model = Cuenta
        fields = "__all__"
        read_only_fields = ("id", "usuario", "total_efectivo")

    def get_total_efectivo(self, obj):
        total = 0 

        total += obj.b_Q100 * 100
        total += obj.b_Q50 * 50
        total += obj.b_Q20 * 20
        total += obj.b_Q10 * 10
        total += obj.b_Q5 * 5
        total += obj.m_100c
        total += obj.m_50c * 50 / 100
        total += obj.m_25c * 25 / 100
        total += obj.m_10c * 10 / 100
        total += obj.m_5c * 5 / 100

        return Decimal(total).quantize(Decimal('0.00'))
    
    def get_diferencia_efectivo(self, obj):
        return self.get_total_efectivo(obj) 
    
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
