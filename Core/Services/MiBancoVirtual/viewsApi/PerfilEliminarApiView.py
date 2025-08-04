from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers import PerfilEliminarSerializer
from ..commands import PerfilEliminarCommand
from ..commandsHandlers import PerfilEliminarCommandHandler
from ..models import Perfil

class PerfilEliminarApiView(DestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilEliminarSerializer
    permission_classes = (IsAuthenticated,)

    # def perform_destroy(self, serializer):
    #     command = PerfilEliminarCommand(
    #         IdPerfil = serializer.validated_data["IdPerfil"],
    #     )

    #     PerfilEliminarCommandHandler().handle(command)

    # def destroy(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_destroy(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)