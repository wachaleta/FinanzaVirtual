from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Value, F
from django.db.models.functions import Concat
from django.db.models.query import QuerySet

from ..models import *
from ..serializers import *
    
class TransferenciaViewSet(viewsets.ModelViewSet):
    
    serializer_class = TransferenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id
        fechaInicio = self.request.query_params.get("fechaInicio")
        fechaFinal = self.request.query_params.get("fechaFinal")

        lista_perfiles = Perfil.objects.filter(usuario = idUsuario)
        lista_cuentas = Cuenta.objects.filter(usuario = idUsuario)

        lista_transferencias = Transaccion.objects.filter(
                #   Validar que sea transaccion
                Q(perfilOrdenante__isnull = False) | Q(cuentaOrdenante__isnull = False),
                Q(perfilBeneficiario__isnull = False) | Q(cuentaBeneficiaria__isnull = False),

                #   Validar que sean del usuario
                Q(perfilOrdenante__in = lista_perfiles) | Q(perfilOrdenante__isnull = True),
                Q(perfilBeneficiario__in = lista_perfiles) | Q(perfilBeneficiario__isnull = True),
                Q(cuentaOrdenante__in = lista_cuentas) | Q(cuentaOrdenante__isnull = True),
                Q(cuentaBeneficiaria__in = lista_cuentas) | Q(cuentaBeneficiaria__isnull = True),

                #   Validar el rango de fechas
                fecha__gte = fechaInicio,
                fecha__lte = fechaFinal
        )

        return lista_transferencias.annotate(
            ordenante_nombre = Concat(
                F("cuentaOrdenante__nombre"),
                Value(" - "),
                F("perfilOrdenante__nombre")
            )
        ).annotate(
            beneficiario_nombre = Concat(
                F("cuentaBeneficiaria__nombre"),
                Value(" - "),
                F("perfilBeneficiario__nombre")
            )
        )