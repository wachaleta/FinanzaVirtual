from rest_framework import serializers
from ..models import *

class TransferenciaSerializer(serializers.ModelSerializer):
    TransferenciaEntrePerfiles = serializers.BooleanField(write_only=True, default=False)
    # ordenante_nombre = serializers.CharField(read_only = True)
    # beneficiario_nombre = serializers.CharField(read_only = True)
    # categoria_nombre = serializers.CharField()
    
    def validate(self, attrs):
        transferencia = attrs.get('TransferenciaEntrePerfiles')
        cuenta_ordenante = attrs.get('IdCuentaOrdenante')
        perfil_ordenante = attrs.get('IdPerfilOrdenante')
        perfil_beneficiario = attrs.get('IdPerfilBeneficiario')
        cuenta_beneficiario = attrs.get('IdCuentaBeneficiaria')

        errores = {}
        
        if transferencia and not perfil_beneficiario:
            errores.update({"IdPerfilBeneficiario": "Este campo es requerido"})
        
        if transferencia and not perfil_ordenante:
            errores.update({"IdPerfilOrdenante": "Este campo es requerido"})
        
        if not transferencia and not cuenta_ordenante:
            errores.update({"IdCuentaOrdenante": "Este campo es requerido"})
        
        if not transferencia and not cuenta_beneficiario:
            errores.update({"IdCuentaBeneficiaria": "Este campo es requerido"})

        if len(errores):
            raise serializers.ValidationError(errores)
        
        return attrs
    
    class Meta: 

        model = Transaccion
        fields = "__all__"
        read_only_fields = ("id", "ordenente_nombre", "beneficiario_nombre", "categoria_nombre")