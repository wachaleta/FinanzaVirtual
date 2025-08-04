from rest_framework import serializers

from ..models import Perfil

class PerfilEliminarSerializer(serializers.Serializer):
    IdPerfil = serializers.IntegerField()

    class Meta:
        model = Perfil
        fields = "__all__"