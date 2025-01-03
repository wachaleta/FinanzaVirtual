from rest_framework import serializers
from ..models import *

class PerfilSerializer(serializers.ModelSerializer):
    saldo = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta: 
        model = Perfil
        fields = "__all__"
        read_only_fields = ("id", "usuario", "saldo")

    def create(self, validated_data):
        x = Perfil.objects.create(
            nombre = validated_data["nombre"],
            agregarTotal = validated_data["agregarTotal"],
            usuario = self.context["request"].user
        )
        return x

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

        lista_subcuentas = Subcuenta.objects.filter(perfil=instance.id)

        for subcuenta in lista_subcuentas:
            
            subcuenta.cambiar_nombre()
            subcuenta.save()



        return instance
