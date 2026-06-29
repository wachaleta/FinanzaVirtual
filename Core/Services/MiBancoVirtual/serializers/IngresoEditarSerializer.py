from rest_framework import serializers
from ..models import *

class IngresoEditarSerializer(serializers.ModelSerializer):
    perfil_ordenante = serializers.PrimaryKeyRelatedField(
        queryset=Perfil.objects.all(),
        required=True
    )
    cuenta_ordenante = serializers.PrimaryKeyRelatedField(
        queryset=Cuenta.objects.all(),
        required=True
    )
    class Meta: 
        model = Transaccion
        fields = (
            "monto",
            "descripcion",
            "fecha",
            "perfil_ordenante",
            "cuenta_ordenante",
            "categoria",
        )
        read_only_fields = ("id",)