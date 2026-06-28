from rest_framework import serializers

from Core.Services.MiBancoVirtual import models

class PerfilSerializer(serializers.ModelSerializer):
    saldo = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, allow_null=False)

    def validate_nombre(self, value):
        user = self.context['request'].user

        query = models.Perfil.objects.filter(nombre__iexact=value, usuario=user)

        if self.instance:
            query = query.exclude(id=self.instance.id)

        repetido = query.exists()

        if repetido:
            raise serializers.ValidationError("Ese nombre se encuentra repetido")

        return value

    class Meta: 
        model = models.Perfil
        fields = "__all__"
        read_only_fields = ("id", "usuario", "saldo")