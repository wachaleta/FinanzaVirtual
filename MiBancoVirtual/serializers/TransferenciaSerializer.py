from rest_framework import serializers
from ..models import *

class TransferenciaSerializer(serializers.ModelSerializer):
    ordenante_nombre = serializers.CharField(read_only = True)
    beneficiario_nombre = serializers.CharField(read_only = True)
    # categoria_nombre = serializers.CharField()
    class Meta: 

        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id", "ordenente_nombre", "beneficiario_nombre", "categoria_nombre")