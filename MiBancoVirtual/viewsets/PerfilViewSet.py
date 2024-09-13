from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response

from ..models import *
from ..serializers import *

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):

        idUsuario = self.request.user.id
        
        return Perfil.objects.raw("""
            SELECT 
                perfil.id,
                perfil.nombre,
                IFNULL( 
                    SUM(
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
                        ) 
                    ),0
                )
                AS saldo
            FROM MiBancoVirtual_perfil perfil
            LEFT JOIN MiBancoVirtual_subcuenta subcuenta ON subcuenta.perfil_id = perfil.id 
            WHERE perfil.usuario_id = %s
            GROUP BY perfil.id
            ORDER BY perfil.nombre ASC
        """, [idUsuario])