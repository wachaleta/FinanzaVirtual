from rest_framework import serializers
from ....Application.Behaviours import Validator
from ..models import *

class PerfilSerializer(serializers.ModelSerializer):
    Nombre = serializers.CharField(allow_null=True, allow_blank=True)
    Saldo = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, allow_null=False)

    class Meta: 
        model = Perfil
        fields = "__all__"
        read_only_fields = ("id", "IdUsuario", "Saldo")

    def create(self, validated_data):
        x = Perfil.objects.create(
            Nombre = validated_data["Nombre"],
            AgregarTotal = validated_data["AgregarTotal"],
            IdUsuario = self.context["request"].user
        )
        return x