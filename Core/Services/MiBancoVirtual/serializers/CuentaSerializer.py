from rest_framework import serializers
from ..models import *

class CuentaSerializer(serializers.ModelSerializer):
    Nombre = serializers.CharField(allow_null=True)
    SaldoTotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    SaldoCalculado = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta: 
        model = Cuenta
        fields = "__all__"
        read_only_fields = ("IdCuenta", "IdUsuario", "SaldoTotal")
    
    def create(self, validated_data):
        
        instance = Cuenta.objects.create(
            Nombre = validated_data["Nombre"],
            SaldoReal = validated_data["SaldoReal"],
            EsEfectivo = validated_data["EsEfectivo"],
            BQ100 = validated_data["BQ100"],
            BQ50 = validated_data["BQ50"],
            BQ20 = validated_data["BQ20"],
            BQ10 = validated_data["BQ10"],
            BQ5 = validated_data["BQ5"],
            M100c = validated_data["M100c"],
            M50c = validated_data["M50c"],
            M25c = validated_data["M25c"],
            M10c = validated_data["M10c"],
            M5c = validated_data["M5c"],
            IdUsuario = self.context["request"].user
        )

        return instance
