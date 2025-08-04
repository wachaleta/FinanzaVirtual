from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers import PerfilCrearSerializer
from ..commands import PerfilCrearCommand
from ..commandsHandlers import PerfilCrearCommandHandler

class PerfilCrearApiView(CreateAPIView):
    serializer_class = PerfilCrearSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        command = PerfilCrearCommand(
            Nombre = serializer.data['Nombre'],
            AgregarTotal = serializer.data['AgregarTotal'],
            IdUsuario = self.request.user
        )

        return PerfilCrearCommandHandler().handle(command)