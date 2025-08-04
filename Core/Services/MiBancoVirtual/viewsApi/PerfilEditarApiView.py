from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers import PerfilEditarSerializer
from ..commands import PerfilEditarCommand
from ..commandsHandlers import PerfilEditarCommandHandler

class PerfilEditarApiView(UpdateAPIView):
    serializer_class = PerfilEditarSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        command = PerfilEditarCommand(
            IdPerfil = serializer.validated_data['IdPerfil'],
            Nombre = serializer.validated_data['Nombre'],
            AgregarTotal = serializer.validated_data['AgregarTotal'],
        )

        handler = PerfilEditarCommandHandler()

        return handler.execute(command)
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        response_data = self.perform_update(serializer)
        
        return Response(response_data, status=status.HTTP_200_OK)