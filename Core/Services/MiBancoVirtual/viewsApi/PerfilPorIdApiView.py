from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers import PerfilCrearSerializer
from ..Queries import PerfilPorIdQuery
from ..QueryHandlers import PerfilPorIdQueryHandler

class PerfilCrearApiView(CreateAPIView):
    serializer_class = PerfilCrearSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, serializer, IdUsuario):
        command = PerfilPorIdQuery(
            Nombre = serializer.validated_data['Nombre'],
            AgregarTotal = serializer.validated_data['AgregarTotal'],
            IdUsuario = IdUsuario
        )

        handler = PerfilPorIdQueryHandler()

        return handler.execute(command)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        response_data = self.get_object(serializer, self.request.user)
        
        return Response(response_data, status=status.HTTP_200_OK)