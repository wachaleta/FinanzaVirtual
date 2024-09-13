from rest_framework import serializers
from ..models import *

class TransaccionPorSubcuentaSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta: 
        model = Transaccion
        fields = ("id", "monto", "descripcion", "fecha", "ordenante_id", "beneficiario_id", "categoria_id", "total")
        read_only_fields = ("id", "total")
