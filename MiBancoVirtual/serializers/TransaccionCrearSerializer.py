from rest_framework import serializers
from ..models import *

class TransaccionCrearSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id",)
