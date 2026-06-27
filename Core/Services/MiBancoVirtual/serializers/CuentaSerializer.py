from rest_framework import serializers

from Core.Services.MiBancoVirtual import models

class CuentaSerializer(serializers.ModelSerializer):
    Nombre = serializers.CharField(allow_null=True)
    SaldoTotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    SaldoCalculado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    def validate_Nombre(self, value):
        user = self.context['request'].user

        repetido = models.Cuenta.objects.filter(Nombre__iexact=value, IdUsuario=user).exists()

        if repetido:
            raise serializers.ValidationError("Ese nombre se encuentra repetido")

        return value

    class Meta: 
        model = models.Cuenta
        fields = "__all__"
        read_only_fields = ("IdCuenta", "IdUsuario", "SaldoTotal")
