from rest_framework import serializers
from ..models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = "__all__"
        read_only_fields = ("IdCategoria", "IdUsuario")

    def create(self, validated_data):
        x = Categoria.objects.create(
            Nombre = validated_data["Nombre"],
            IdUsuario = self.context["request"].user
        )
        return x
