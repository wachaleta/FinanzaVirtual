from rest_framework import serializers
from ..models import *

class GastoSerializer(serializers.ModelSerializer):
    # subcuenta = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(read_only=True)
    categoria_nombre = serializers.CharField(read_only=True)
    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)
