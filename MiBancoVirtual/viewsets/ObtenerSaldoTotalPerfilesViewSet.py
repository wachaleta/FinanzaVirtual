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

        lista_perfiles = Perfil.objects.filter(usuario=idUsuario)

        lista_perfiles = filter(lambda x: x.agregarTotal or x.saldo < 0, lista_perfiles)

        saldo_total = sum(list(map(lambda x: x.saldo, lista_perfiles)))

        saldo_total = round(Decimal(saldo_total), 2)

        return Response({'saldo': saldo_total})
