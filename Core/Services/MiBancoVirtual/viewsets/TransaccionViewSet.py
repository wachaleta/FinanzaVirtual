from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransaccionSerializer

from Core.Services.MiBancoVirtual.Funciones import TransaccionFunciones

class TransaccionViewSet(FinanzasModelViewSet):
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        lista_transacciones = Transaccion.objects.filter(
                Q(perfil_ordenante__usuario = idUsuario) | Q(perfil_beneficiario__usuario = idUsuario) |
                Q(cuenta_ordenante__usuario = idUsuario) | Q(cuenta_beneficiaria__usuario = idUsuario) 
            )
        
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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     transaccion = TransaccionFunciones.transaccion_crear(
    #         usuario=request.user,
    #         **serializer.validated_data,
    #     )

    #     return Response({'id': transaccion.id}, status=status.HTTP_201_CREATED)
    def destroy(self, request, *args, **kwargs):
        transaccion = self.get_object()

        id = TransaccionFunciones.transaccion_eliminar(
            usuario=request.user,
            transaccion=transaccion,
        )

        return Response({'id': id}, status=status.HTTP_201_CREATED)