from rest_framework import serializers
from ..models import TransaccionProgramadaDetalle
from . import *

class TransaccionProgramadaDetalleSerializer(serializers.ModelSerializer):
    Categoria = CategoriaSerializer()

    class Meta:
        model = TransaccionProgramadaDetalle
        fields = "__all__"
        read_only_fields = ('Categoria',)