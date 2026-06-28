from rest_framework import serializers
from ....Application.Behaviours import Validator
from ..models import *

class PerfilSerializer(serializers.ModelSerializer):
    saldo = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, allow_null=False)

    class Meta: 
        model = Perfil
        fields = "__all__"
        read_only_fields = ("id", "usuario", "saldo")