from rest_framework import serializers
from ..models import *

from Core.Services.MiBancoVirtual.serializers.PerfilSerializer import PerfilSerializer
from Core.Services.MiBancoVirtual.serializers.CuentaSerializer import CuentaSerializer

class GastoSerializer(serializers.ModelSerializer):
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
        fields = "__all__"
        read_only_fields = ("id",)