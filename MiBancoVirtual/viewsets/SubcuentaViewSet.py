from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Coalesce, Concat
from django.db.models import Sum, Subquery, OuterRef, Value, DecimalField, CharField, Case, When, F

from ..models import *
from ..serializers import *

class SubcuentaViewSet(viewsets.ModelViewSet):
    serializer_class = SubcuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        idUsuario = self.request.user.id

        subcuentas = Subcuenta.objects.filter(cuenta__usuario = idUsuario)

        return subcuentas.annotate(
            #   Agrega el saldo total en las subcuentas por las transacciones
            saldo =
                Coalesce(
                    Subquery(
                        Transaccion.objects.filter(
                            beneficiario_id__in=OuterRef("id")
                        ).values("beneficiario").annotate(
                            total=Sum('monto', default=0)  
                        ).values('total'),
                        default=0,
                        output_field=DecimalField(default=0)
                    ),
                    Value(0, DecimalField())
                )
                -
                Coalesce(
                    Subquery(
                        Transaccion.objects.filter(
                            ordenante_id__in=OuterRef("id")
                        ).values("ordenante").annotate(
                            total=Sum('monto', default=0)  
                        ).values('total'),
                        default=0,
                        output_field=DecimalField(default=0)
                    ),
                    Value(0, DecimalField())
                )
        ).annotate(
            #   Agrega el nombre juntando el de la cuenta y el perfil
            subcuenta_nombre = Concat(
                F("cuenta__nombre"), 
                Value(" - "),
                F("perfil__nombre")
            ) 
        ).order_by("-saldo")
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
