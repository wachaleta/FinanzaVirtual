from rest_framework import serializers

from Core.Services.MiBancoVirtual import models

class CuentaEditarSerializer(serializers.ModelSerializer):
    
    def validate_nombre(self, value):

        user = self.context['request'].user

        repetido = models.Cuenta.objects.filter(nombre__iexact=value, usuario=user).exclude(pk=self.instance.pk).exists()

        if repetido:
            raise serializers.ValidationError("Ese nombre se encuentra repetido")

        return value
    
    class Meta: 
        model = models.Cuenta
        fields = "__all__"
        read_only_fields = (
            'usuario',
        )
