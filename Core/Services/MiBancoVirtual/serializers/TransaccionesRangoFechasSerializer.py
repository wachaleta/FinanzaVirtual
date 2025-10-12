from rest_framework import serializers
from ..models import *

class TransaccionesRangoFechasSerializer(serializers.ModelSerializer):
    CategoriaNombre = serializers.CharField(read_only=True)
    ordenante_nombre = serializers.CharField(read_only= True)
    beneficiario_nombre = serializers.CharField(read_only= True)
    
    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)