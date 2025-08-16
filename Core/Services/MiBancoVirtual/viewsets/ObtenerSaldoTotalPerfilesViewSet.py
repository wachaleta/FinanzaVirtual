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

        lista_perfiles = Perfil.objects.filter(IdUsuario=idUsuario)

        lista_perfiles_suman = filter(lambda x: x.AgregarTotal or x.Saldo < 0, lista_perfiles)

        saldo_suma = sum(list(map(lambda x: x.Saldo, lista_perfiles_suman)))
        saldo_suma = round(Decimal(saldo_suma), 2)

        lista_perfiles_no_suman = filter(lambda x: not x.AgregarTotal and x.Saldo >= 0, lista_perfiles)
        saldo_no_suma = sum(list(map(lambda x: x.Saldo, lista_perfiles_no_suman)))
        saldo_no_suma = round(Decimal(saldo_no_suma), 2)

        saldo_total = saldo_suma + saldo_no_suma

        return Response(
            {
                'SaldoTotal': saldo_total,
                'SaldoSuma': saldo_suma,
                'SaldoNoSuma': saldo_no_suma
            }
        )
