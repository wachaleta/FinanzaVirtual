from rest_framework import serializers

from Core.Services.MiBancoVirtual import models

from Core.Services.MiBancoVirtual.serializers.CuentaEfectivoSerializer import CuentaEfectivoSerializer

class CuentaSerializer(serializers.ModelSerializer):
    efectivo = serializers.DictField(write_only=True)
    cuentaefectivo_set = CuentaEfectivoSerializer(many=True, read_only=True)
    saldo_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    saldo_real_calculado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    def validate_nombre(self, value):
        user = self.context['request'].user

        repetido = models.Cuenta.objects.filter(nombre__iexact=value, usuario=user).exists()

        if repetido:
            raise serializers.ValidationError("Ese nombre se encuentra repetido")

        return value

    class Meta: 
        model = models.Cuenta
        exclude = (
            "bQ100",
            "bQ50",
            "bQ20",
            "bQ10",
            "bQ5",
            "m100c",
            "m50c",
            "m25c",
            "m10c",
            "m5c",
        )
        read_only_fields = ("id", "usuario", "saldo_total")
