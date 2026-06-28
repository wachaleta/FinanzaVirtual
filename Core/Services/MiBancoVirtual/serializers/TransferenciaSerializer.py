from rest_framework import serializers
from ..models import *

class TransferenciaSerializer(serializers.ModelSerializer):
    transferencia_entre_perfiles = serializers.BooleanField(write_only=True, default=False)
    # ordenante_nombre = serializers.CharField(read_only = True)
    # beneficiario_nombre = serializers.CharField(read_only = True)
    # categoria_nombre = serializers.CharField()
    
    def validate(self, attrs):
        transferencia_entre_perfiles = attrs.get('transferencia_entre_perfiles')
        cuenta_ordenante = attrs.get('cuenta_ordenante')
        perfil_ordenante = attrs.get('perfil_ordenante')
        perfil_beneficiario = attrs.get('perfil_beneficiario')
        cuenta_beneficiario = attrs.get('cuenta_beneficiaria')

        errores = {}
        
        if transferencia_entre_perfiles:
            if not perfil_beneficiario:
                errores.update({"perfil_beneficiario": "Este campo es requerido"})
        
            if not perfil_ordenante:
                errores.update({"perfil_ordenante": "Este campo es requerido"})

            if perfil_beneficiario == perfil_ordenante:
                errores.update({"perfil_ordenante": "Los perfiles no pueden ser iguales"})
                errores.update({"perfil_beneficiario": "Los perfiles no pueden ser iguales"})

        
        if not transferencia_entre_perfiles:
            if not cuenta_ordenante:
                errores.update({"cuenta_ordenante": "Este campo es requerido"})
        
            if not cuenta_beneficiario:
                errores.update({"cuenta_beneficiaria": "Este campo es requerido"})

            if cuenta_ordenante == cuenta_beneficiario:
                errores.update({"cuenta_ordenante": "Las cuentas no pueden ser iguales"})
                errores.update({"cuenta_beneficiario": "Las cuentas no pueden ser iguales"})


        if len(errores):
            raise serializers.ValidationError(errores)
        
        return attrs
    
    class Meta: 

        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id", "ordenente_nombre", "beneficiario_nombre", "categoria_nombre")