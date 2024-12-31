from rest_framework import serializers
from ..models import TransaccionProgramadaDetalle
from . import *

class TransaccionProgramadaDetalleSerializer(serializers.ModelSerializer):
    Categoria = CategoriaSerializer()
    Ordenante = SubcuentaSerializer()
    Beneficiario = SubcuentaSerializer()

    class Meta:
        model = TransaccionProgramadaDetalle
        fields = "__all__"
        read_only_fields = ('Categoria',)