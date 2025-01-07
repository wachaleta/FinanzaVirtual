from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Coalesce
from django.db.models import Sum, Subquery, OuterRef, Value, DecimalField, Case, When, F
from decimal import Decimal

from ..models import *
from ..serializers import *

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        idUsuario = self.request.user.id

        cuentas = Cuenta.objects.filter(usuario = idUsuario)

        return cuentas.annotate(
            # Agregar el saldo total de las transacciones en cada cuenta
            saldo_total =
                Coalesce(
                    Subquery(
                        Transaccion.objects.filter(
                            beneficiario__cuenta_id__in=OuterRef("id")
                        ).values("beneficiario__cuenta").annotate(
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
                            ordenante__cuenta_id__in=OuterRef("id")
                        ).values("ordenante__cuenta").annotate(
                            total=Sum('monto', default=0)  
                        ).values('total'),
                        default=0,
                        output_field=DecimalField(default=0)
                    ),
                    Value(0, DecimalField())
                )
        ).annotate(
            # Si es efectivo toma el cálculo de las unidades del efectivo, si no toma el valor real
            saldo_mostrar = 
            Case(
                When(es_efectivo = True, then=
                    F('b_Q100') * Decimal(100)+
                    F("b_Q50") * Decimal(50)+
                    F("b_Q20") * Decimal(20)+
                    F("b_Q10") * Decimal(10)+
                    F("b_Q5")  * Decimal(5)+
                    F("m_100c") +
                    F("m_50c")  * Decimal(0.5)+
                    F("m_25c") * Decimal(0.25)+
                    F("m_10c") * Decimal(0.1)+
                    F("m_5c") * Decimal(0.05)
                ),
                default=F("saldo_real")
            )
        )