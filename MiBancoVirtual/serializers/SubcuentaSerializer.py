from rest_framework import serializers
from ..models import *

class SubcuentaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Subcuenta
        fields = "__all__"
        read_only_fields = ("id", "nombre")

    def create(self, validated_data):

        instance = super().create(validated_data)

        instance.perfil.calcular_saldo()
        instance.cuenta.calcular_saldo()
        instance.cambiar_nombre()

        return instance
    
    def update(self, instance, validated_data):
        super().update(instance, validated_data)

        instance.perfil.calcular_saldo()
        instance.cuenta.calcular_saldo()

        return instance
