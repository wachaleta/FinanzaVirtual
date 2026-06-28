from decimal import Decimal
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Q, F
from django.db.models.functions import Coalesce
from rest_framework.response import Response

from ..models import *
from ..serializers import *

class ObtenerSaldoTotalPerfilesViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = self.request.user

        perfiles = Perfil.objects.filter(usuario=user).annotate(
            saldo=Coalesce(
                Sum('transaccion_perfil_beneficiario__Monto'), Decimal(0)
            )-
            Coalesce(
                Sum('transaccion_perfil_ordenante__Monto'), Decimal(0)
            )
        )

        perfilesDisponible = perfiles.filter(
            Q(suma_disponible=True)
            | Q(saldo__lt=0)
        )

        saldoDisponible = perfilesDisponible.aggregate(
            saldo_disponible = Sum('saldo')
        )['saldo_disponible'] or 0.0

        # saldoDisponible = sum(list(map(lambda x: x.Saldo, perfilesDisponible)))
        # saldoDisponible = round(Decimal(saldoDisponible), 2)

        saldo_no_disponible = perfiles.filter(
            suma_disponible=False,
            saldo__gte=0
        ).aggregate(
            saldo_no_disponible=Sum('saldo')
        )['saldo_no_disponible'] or 0.0


        saldo_total = saldoDisponible + saldo_no_disponible

        return Response(
            {
                'SaldoTotal': saldo_total,
                'SaldoDisponible': saldoDisponible,
                'SaldoNoDisponible': saldo_no_disponible
            }
        )
