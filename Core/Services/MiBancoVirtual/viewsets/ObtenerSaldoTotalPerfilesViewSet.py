from decimal import Decimal
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.response import Response

from ..models import *
from ..serializers import *

class ObtenerSaldoTotalPerfilesViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        idUsuario = self.request.user.id

        perfiles = Perfil.objects.filter(IdUsuario=idUsuario)

        perfilesDisponible = filter(lambda x: x.SumaDisponible or x.Saldo < 0, perfiles)

        saldoDisponible = sum(list(map(lambda x: x.Saldo, perfilesDisponible)))
        saldoDisponible = round(Decimal(saldoDisponible), 2)

        perfilesNoDisponible = filter(lambda x: not x.SumaDisponible and x.Saldo >= 0, perfiles)
        saldoNoDisponible = sum(list(map(lambda x: x.Saldo, perfilesNoDisponible)))
        saldoNoDisponible = round(Decimal(saldoNoDisponible), 2)

        saldo_total = saldoDisponible + saldoNoDisponible

        return Response(
            {
                'SaldoTotal': saldo_total,
                'SaldoDisponible': saldoDisponible,
                'SaldoNoDisponible': saldoNoDisponible
            }
        )
