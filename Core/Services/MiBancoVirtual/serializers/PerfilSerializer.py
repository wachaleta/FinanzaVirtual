from rest_framework import serializers
from ..models import *

class PerfilSerializer(serializers.ModelSerializer):
    Saldo = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, allow_null=False)

    class Meta: 
        model = Perfil
        fields = "__all__"
        read_only_fields = ("id", "usuario", "Saldo")

    def create(self, validated_data):
        x = Perfil.objects.create(
            nombre = validated_data["nombre"],
            agregarTotal = validated_data["agregarTotal"],
            usuario = self.context["request"].user
        )
        return x
