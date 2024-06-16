from rest_framework import serializers
from ..models import *

class PerfilCrearSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Perfil
        fields = "__all__"
        read_only_fields = ("id", "usuario")

    def create(self, validated_data):

        objeto = Perfil.objects.create(
            nombre = validated_data["nombre"],
            usuario = self.context["request"].user
        )
        
        return objeto
