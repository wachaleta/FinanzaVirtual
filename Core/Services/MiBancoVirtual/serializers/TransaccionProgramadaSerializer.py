from rest_framework import serializers
from ..models import TransaccionProgramada
from .TransaccionProgramadaDetalleSerializer import TransaccionProgramadaDetalleSerializer

class TransaccionProgramadaSerializer(serializers.ModelSerializer):
    Detalles = TransaccionProgramadaDetalleSerializer(
        source='transaccionprogramadadetalle_set', many=True, read_only=True
    )
    
    class Meta:
        model = TransaccionProgramada
        fields = "__all__"
        read_only_fields = ('Usuario', 'Detalles')

    def create(self, validated_data):

        fecha = validated_data.get("fecha_limite", None)
        # if(validated_data["fecha_limite"] != None):

        nuevo = TransaccionProgramada.objects.create(
            Nombre = validated_data["Nombre"],
            fecha_limite = fecha,
            
            Usuario = self.context["request"].user
        )
        return nuevo