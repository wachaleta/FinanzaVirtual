from rest_framework import serializers

from Core.Services.MiBancoVirtual import models

class CuentaEfectivoSerializer(serializers.ModelSerializer):
    valor = serializers.DecimalField(max_digits=5, decimal_places=2, source='efectivo_moneda.valor')

    class Meta: 
        model = models.CuentaEfectivo
        fields = "__all__"
        read_only_fields = ("id", "usuario")
