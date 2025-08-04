from rest_framework import serializers
from ..models import *

class TransaccionCrearSerializer(serializers.ModelSerializer):
    cuenta_ordenante_nombre = serializers.CharField(read_only= True)
    perfil_ordenante_nombre = serializers.CharField(read_only= True)
    cuenta_beneficiario_nombre = serializers.CharField(read_only= True)
    perfil_beneficiario_nombre = serializers.CharField(read_only= True)
    ordenante_nombre = serializers.CharField(read_only= True)
    beneficiario_nombre = serializers.CharField(read_only= True)
    
    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)

    def validate_monto(self, value):
        if value == 0:
            raise serializers.ValidationError("El monto no puede ser igual a 0")
        
        return value