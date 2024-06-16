from rest_framework import serializers
from ..models import *

class TransferenciaSerializer(serializers.ModelSerializer):
    nombre_ordenante = serializers.CharField(source="ordenante.nombre", read_only=True)
    nombre_beneficiario = serializers.CharField(source="beneficiario.nombre", read_only=True)
    class Meta: 
        model = Transferencia
        fields = "__all__"
        read_only_fields = ("id", "nombre_ordenante", "nombre_benefiaciario")