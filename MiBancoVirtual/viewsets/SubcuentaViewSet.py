from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..serializers import *

class SubcuentaViewSet(viewsets.ModelViewSet):
    serializer_class = SubcuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        idUsuario = self.request.user.id

        return Subcuenta.objects.raw("""
            SELECT 
                subcuenta.id,
                IFNULL(
                    (
                        SELECT 
                            SUM(	
                                CASE
                                    WHEN transaccion.ordenante_id = subcuenta.id THEN - transaccion.monto 
                                    WHEN transaccion.beneficiario_id = subcuenta.id THEN transaccion.monto 
                                END
                            ) as Saldo 
                        FROM MiBancoVirtual_transaccion transaccion
                    ), 0
                ) AS saldo,
                (cuenta.nombre || " - " || perfil.nombre) as subcuenta_nombre,
                subcuenta.cuenta_id as idCuenta,
                cuenta.nombre as cuenta_nombre,
                subcuenta.perfil_id as idPerfil,
                perfil.nombre as perfil_nombre
            FROM MiBancoVirtual_subcuenta subcuenta
            INNER JOIN MiBancoVirtual_cuenta cuenta on cuenta.id = subcuenta.cuenta_id 
            INNER JOIN auth_user usuario on usuario.id = cuenta.usuario_id 
            INNER JOIN MiBancoVirtual_perfil perfil on perfil.id = subcuenta.perfil_id 
            WHERE usuario.id = %s   
        """, [idUsuario])
