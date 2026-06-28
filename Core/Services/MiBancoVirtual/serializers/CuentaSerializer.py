from rest_framework import serializers

from Core.Services.MiBancoVirtual import models

class CuentaSerializer(serializers.ModelSerializer):
    saldo_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    saldo_efectivo_calculado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    def validate_nombre(self, value):
        user = self.context['request'].user

        repetido = models.Cuenta.objects.filter(nombre__iexact=value, usuario=user).exists()

        if repetido:
            raise serializers.ValidationError("Ese nombre se encuentra repetido")

        return value

    class Meta: 
        model = models.Cuenta
        fields = "__all__"
        read_only_fields = ("id", "usuario", "saldo_total")
