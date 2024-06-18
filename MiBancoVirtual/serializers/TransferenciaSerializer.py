from rest_framework import serializers
from ..models import *

class TransferenciaSerializer(serializers.ModelSerializer):
    nombre_ordenante = serializers.CharField(source="ordenante.nombre", read_only=True)
    nombre_beneficiario = serializers.CharField(source="beneficiario.nombre", read_only=True)
    class Meta: 
        model = Transferencia
        fields = "__all__"
        read_only_fields = ("id", "nombre_ordenante", "nombre_benefiaciario")

    def create(self, validated_data):
        instance = super().create(validated_data)

        instance.ordenante.crear_transferencia(instance.beneficiario, instance.monto)

        return instance
    
    def update(self, instance, validated_data):
        
        #   Regresa la transferencia anterior
        instance.beneficiario.crear_transferencia(instance.ordenante, instance.monto)

        #   Modifica la transferencia
        super().update(instance, validated_data)
        
        #   Crea la nueva transferencia
        Ordenante = Subcuenta.objects.filter(id=instance.ordenante.id).first()
        Beneficiario = Subcuenta.objects.filter(id=instance.beneficiario.id).first()
        
        Ordenante.crear_transferencia(Beneficiario, instance.monto)

        return instance