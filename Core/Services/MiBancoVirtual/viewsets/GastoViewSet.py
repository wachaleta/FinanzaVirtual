from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import GastoSerializer, GastoEditarSerializer
from ..validators import GastoCrearValidator, GastoEditarValidator

from Core.Services.MiBancoVirtual.Funciones import TransaccionFunciones
class GastoViewSet(FinanzasModelViewSet):
    serializer_class = GastoSerializer
    create_validator = GastoCrearValidator
    update_validator = GastoEditarValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id
        # fechaInicio = self.request.query_params.get("fechaInicio")
        # fechaFinal = self.request.query_params.get("fechaFinal")

        lista_transacciones = Transaccion.objects.filter(
                Q(perfil_ordenante__usuario = idUsuario) | Q(perfil_beneficiario__usuario = idUsuario) |
                Q(cuenta_ordenante__usuario = idUsuario) | Q(cuenta_beneficiaria__usuario = idUsuario) 
            )
        # .filter(fecha__gte = fechaInicio).filter(fecha__lte = fechaFinal)
        
        return lista_transacciones.annotate(
            ordenante_nombre = Concat(
                F("cuenta_ordenante__nombre"), 
                Value(" - "),
                F("perfil_ordenante__nombre")
            )
        ).annotate(
            beneficiario_nombre = Concat(
                F("cuenta_beneficiaria__nombre"), 
                Value(" - "),
                F("perfil_beneficiario__nombre")
            )
        ).order_by("-fecha", "-fecha_creacion")

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaccion = TransaccionFunciones.gasto_crear(
            usuario=request.user,
            **serializer.validated_data,
        )

        return Response({'id': transaccion.id}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        transaccion = self.get_object()

        serializer = GastoEditarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaccion = TransaccionFunciones.gasto_editar(
            usuario=request.user,
            transaccion=transaccion,
            **serializer.validated_data,
        )

        return Response({'id': transaccion.id}, status=status.HTTP_200_OK)