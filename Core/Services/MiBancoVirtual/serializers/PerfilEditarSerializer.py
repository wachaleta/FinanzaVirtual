from rest_framework import serializers

from ..models import Perfil

class PerfilEditarSerializer(serializers.Serializer):
    IdPerfil = serializers.IntegerField()
    Nombre = serializers.CharField(default="", allow_blank=True)
    AgregarTotal = serializers.BooleanField(default=False)

    class Meta:
        model = Perfil
        fields = "__all__"