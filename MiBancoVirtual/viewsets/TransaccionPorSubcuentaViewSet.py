from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class TransaccionPorSubcuentaViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionPorSubcuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaccion.objects.raw(
            """
            WITH var AS (SELECT %s AS subcuenta)
            SELECT 
            id,
            descripcion,
            monto,
            fecha,
            ordenante_id,
            beneficiario_id,
            categoria_id,
            SUM(
                CASE 
                    when ordenante_id = (SELECT subcuenta FROM var) then -monto
                    when beneficiario_id = (SELECT subcuenta FROM var) then monto
                END
            ) over (order by fecha) as total
            FROM MiBancoVirtual_transaccion mbvt 
            WHERE mbvt.beneficiario_id = (SELECT subcuenta FROM var) or mbvt.ordenante_id = (SELECT subcuenta FROM var)
            ORDER BY fecha, fechaCreacion 
            """, [self.request.query_params.get("idSubcuenta")]
        )