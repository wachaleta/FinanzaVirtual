from rest_framework import serializers
from ..models import *

class IngresoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(read_only = True)
    categoria_nombre = serializers.CharField(read_only = True)

    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)
