from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *

class GastoViewSet(viewsets.ModelViewSet):
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        return Transaccion.objects.raw("""
            SELECT 
                transaccion.id,
                transaccion.monto,
                transaccion.descripcion,
                transaccion.fecha,
                transaccion.categoria_id,
                categoria.nombre as categoria_nombre,
                transaccion.ordenante_id as subcuenta,
                (cuenta.nombre || " - " || perfil.nombre) as subcuenta_nombre,
                transaccion.fechaCreacion 
            FROM MiBancoVirtual_transaccion transaccion
            INNER JOIN MiBancoVirtual_subcuenta subcuenta ON subcuenta.id = transaccion.ordenante_id 
            INNER JOIN MiBancoVirtual_categoria categoria ON categoria.id  = transaccion.categoria_id
            INNER JOIN MiBancoVirtual_perfil perfil ON perfil.id = subcuenta.perfil_id 
            INNER JOIN MiBancoVirtual_cuenta cuenta on cuenta.id = subcuenta.cuenta_id 
            INNER JOIN auth_user usuario ON usuario.id = cuenta.usuario_id 
            WHERE transaccion.beneficiario_id is NULL  AND usuario.id = %s
            ORDER BY transaccion.fechaCreacion DESC, transaccion.fecha DESC
            """, [idUsuario])
