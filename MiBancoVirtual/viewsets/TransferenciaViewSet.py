from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *
    
class TransferenciaViewSet(viewsets.ModelViewSet):
    
    serializer_class = TransferenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        return Transaccion.objects.raw("""
        SELECT 
            transaccion.id,
            transaccion.monto,
            transaccion.descripcion,
            transaccion.fecha,
            transaccion.ordenante_id,
            (cuenta_beneficiario.nombre || " - " || perfil_beneficiario.nombre) as beneficiario_nombre,
            (cuenta_ordenante.nombre || " - " || perfil_ordenante.nombre) as ordenante_nombre,
            transaccion.beneficiario_id,
            transaccion.categoria_id,
            categoria.nombre as categoria_nombre,
            transaccion.fechaCreacion
        from MiBancoVirtual_transaccion transaccion
        inner join MiBancoVirtual_categoria categoria on categoria.id = transaccion.categoria_id
        INNER JOIN MiBancoVirtual_subcuenta beneficiario on beneficiario.id = transaccion.beneficiario_id
        INNER JOIN MiBancoVirtual_cuenta cuenta_beneficiario on cuenta_beneficiario.id = beneficiario.cuenta_id
        INNER JOIN MiBancoVirtual_perfil perfil_beneficiario on perfil_beneficiario.id = beneficiario.perfil_id
        INNER JOIN MiBancoVirtual_subcuenta ordenante on ordenante.id = transaccion.ordenante_id 
        INNER JOIN MiBancoVirtual_cuenta cuenta_ordenante on cuenta_ordenante.id = ordenante.cuenta_id 
        INNER JOIN MiBancoVirtual_perfil perfil_ordenante on perfil_ordenante.id  = ordenante.perfil_id 
        WHERE categoria.usuario_id = %s
        """, [idUsuario])