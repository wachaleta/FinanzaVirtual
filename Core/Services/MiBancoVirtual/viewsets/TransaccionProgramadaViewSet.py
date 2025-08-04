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
                tp.id,
                tp.Nombre,
                tp.FechaCreacion,
                tp.FechaLimite, 
                tp.Usuario_id 
            FROM MiBancoVirtual_transaccionprogramada tp
            WHERE tp.Usuario_id = %s
        """, [idUsuario])