from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Value
from django.db.models.functions import Concat

from ..models import *
from ..serializers import *
    
class IngresoViewSet(viewsets.ModelViewSet):
    
    serializer_class = IngresoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        idUsuario = self.request.user.id

        fechaInicio = self.request.query_params.get("fechaInicio")
        fechaFinal = self.request.query_params.get("fechaFinal")

        lista_cuentas = Cuenta.objects.filter(usuario = idUsuario)
        lista_perfiles = Perfil.objects.filter(usuario = idUsuario)

        lista_ingresos = Transaccion.objects.filter(
            #   Validar que sean del usuario
            cuentaBeneficiaria__in = lista_cuentas,
            perfilBeneficiario__in = lista_perfiles,

            #   Validar que sea ingreso
            cuentaOrdenante__isnull = True,
            perfilOrdenante__isnull = True,

            #   Validar rango de fechas
            fecha__gte = fechaInicio,
            fecha__lte = fechaFinal
        )
        
        return lista_ingresos.annotate(
            nombre = Concat(
                F("cuentaBeneficiaria__nombre"),
                Value(" - "),
                F("perfilBeneficiario__nombre")
            )
        ).annotate(
            categoria_nombre = F("categoria__nombre")
        )