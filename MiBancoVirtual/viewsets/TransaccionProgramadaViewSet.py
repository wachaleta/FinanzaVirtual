from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import TransaccionProgramada
from ..serializers import TransaccionProgramadaSerializer 

class TransaccionProgramadaViewSet(viewsets.ModelViewSet):
    serializer_class = TransaccionProgramadaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        return TransaccionProgramada.objects.raw("""
            SELECT
                tp.Id,
                tp.Monto,
                tp.Descripcion,
                tp.FechaLimite,
                tp.MetaCantidad,
                tp.Abonado,
                tp.FechaCreacion,
                tp.Ordenante_id,
                tp.Beneficiario_id,
                tp.Categoria_id
            FROM MiBancoVirtual_transaccionprogramada tp
            INNER JOIN MiBancoVirtual_categoria categoria on categoria.id = tp.Categoria_id
            WHERE categoria.usuario_id = %s
        """, [idUsuario])