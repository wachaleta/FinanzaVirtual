from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cuenta.objects.raw("""
            SELECT
                cuenta.id,
                cuenta.nombre,
                SUM
                (
                    CASE 
                        WHEN transaccion.ordenante_id = subcuenta.id THEN - transaccion.monto
                        WHEN transaccion.beneficiario_id = subcuenta.id THEN transaccion.monto
                        ELSE 0
                    END
                ) as saldo_total,
                cuenta.es_efectivo,
                cuenta.b_Q100,
                cuenta.b_Q50,
                cuenta.b_Q20,
                cuenta.b_Q10,
                cuenta.b_Q5,
                cuenta.m_100c,
                cuenta.m_50c,
                cuenta.m_25c,
                cuenta.m_10c,
                cuenta.m_5c
            FROM MiBancoVirtual_cuenta cuenta
            LEFT JOIN MiBancoVirtual_subcuenta subcuenta on subcuenta.cuenta_id  = cuenta.id
            LEFT JOIN MiBancoVirtual_transaccion transaccion on transaccion.ordenante_id = subcuenta.id 
            OR transaccion.beneficiario_id = subcuenta.id
            WHERE cuenta.usuario_id = %s
            GROUP BY cuenta.id""", [self.request.user.id])
