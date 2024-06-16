from rest_framework import serializers
from ..models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = "__all__"
        read_only_fields = ("id", "usuario")

    def create(self, validated_data):
        x = Categoria.objects.create(
            nombre = validated_data["nombre"],
            usuario = self.context["request"].user
        )
        return x
