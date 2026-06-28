from rest_framework import serializers

from Core.Services.MiBancoVirtual import models
class CategoriaSerializer(serializers.ModelSerializer):
    def validate_nombre(self, value):
        user = self.context['request'].user

        query = models.Categoria.objects.filter(nombre__iexact=value, usuario=user)

        if self.instance:
            query = query.exclude(id=self.instance.id)

        repetido = query.exists()

        if repetido:
            raise serializers.ValidationError("Ese nombre se encuentra repetido")

        return value
    class Meta: 
        model = models.Categoria
        fields = "__all__"
        read_only_fields = ("id", "usuario")