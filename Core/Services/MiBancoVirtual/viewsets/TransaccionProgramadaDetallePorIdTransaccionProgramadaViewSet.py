from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import TransaccionProgramadaDetalle
from ..serializers import TransaccionProgramadaDetalleSerializer 

class TransaccionProgramadaDetallePorIdTransaccionProgramadaViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionProgramadaDetalleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idTransaccionProgramada = self.request.query_params.get("idTransaccionProgramada")

        return TransaccionProgramadaDetalle.objects.raw("""
            # SELECT
            #     d.Id,
            #     d.Monto,
            #     d.Descripcion,
            #     d.FechaCreacion,
            #     d.Beneficiario_id,
            #     d.Categoria_id,
            #     d.Ordenante_id,
            #     d.TransaccionProgramada_id
            # FROM MiBancoVirtual_transaccionprogramadadetalle d
            # INNER JOIN MiBancoVirtual_transaccionprogramada tp ON tp.Id = d.TransaccionProgramada_id 
            # WHERE tp.Id = %s
        """, [idTransaccionProgramada])