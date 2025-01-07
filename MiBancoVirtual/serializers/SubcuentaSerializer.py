from rest_framework import serializers
from ..models import *
from . import *

class SubcuentaSerializer(serializers.ModelSerializer):
    subcuenta_nombre = serializers.CharField(read_only=True)
    saldo = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta: 
        model = Subcuenta
        fields = "__all__"
        read_only_fields = ("id", "cuenta_nombre", "perfil_nombre", "subcuenta_nombre", "saldo")
