from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from ..Serializers import IniciarSesionSerializer
from ..Commands import IniciarSesionCommand
from ..CommandHandlers import IniciarSesionCommandHandler

class IniciarSesionApiView(CreateAPIView):
    serializer_class = IniciarSesionSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        command = IniciarSesionCommand(
            username = serializer.validated_data['username'],
            password = serializer.validated_data['password']
        )
        
        handler = IniciarSesionCommandHandler()

        response_data = handler.execute(command)

        return response_data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            response_data = self.perform_create(serializer)
            return Response(response_data, status=status.HTTP_200_OK)
        except ValidationError as e:
            # Re-lanzar la excepción para que el middleware pueda manejarla
            raise e
        except Exception as e:
            # Permitir que el middleware maneje otras excepciones
            raise e