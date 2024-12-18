from rest_framework import serializers
from ..models import TransaccionProgramada

class TransaccionProgramadaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TransaccionProgramada
        fields = "__all__"
        read_only_fields = ("Abonado",)