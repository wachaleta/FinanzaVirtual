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
        ).order_by("subcuenta_nombre")