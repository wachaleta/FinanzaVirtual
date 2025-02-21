from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F, Value
from django.db.models.functions import Concat

from ..models import *
from ..serializers import *

class GastoViewSet(viewsets.ModelViewSet):
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        fechaInicio = self.request.query_params.get("fechaInicio")
        fechaFinal = self.request.query_params.get("fechaFinal")

        lista_cuentas = Cuenta.objects.filter(usuario = idUsuario)
        lista_perfiles = Perfil.objects.filter(usuario = idUsuario)

        lista_gastos = Transaccion.objects.filter(
            #   Validar que sean del usuario
            perfilOrdenante__in = lista_perfiles,
            cuentaOrdenante__in = lista_cuentas,

            #   Validar que sea Gasto
            cuentaBeneficiaria__isnull = True,
            perfilBeneficiario__isnull = True,

            #   Validar el rango de fechas
            fecha__gte = fechaInicio,
            fecha__lte = fechaFinal
        )

        return lista_gastos.annotate(
            nombre = Concat(
                F("cuentaOrdenante__nombre"),
                Value(" - "),
                F("perfilOrdenante__nombre")
            )
        ).annotate(
            categoria_nombre = F("categoria__nombre")
        )