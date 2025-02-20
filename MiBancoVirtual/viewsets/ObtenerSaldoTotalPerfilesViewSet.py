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

        lista_perfiles = Perfil.objects.filter(usuario=idUsuario).filter(agregarTotal=True)

        saldo_total = Transaccion.objects.filter(perfilBeneficiario__in = lista_perfiles).aggregate(
            saldo=Sum('monto')
        )['saldo' or 0]

        saldo_total -= Transaccion.objects.filter(perfilOrdenante__in = lista_perfiles).aggregate(
            saldo=Sum('monto')
        )['saldo' or 0]

        saldo_total = round(Decimal(saldo_total), 2)

        return Response({'saldo': saldo_total})
