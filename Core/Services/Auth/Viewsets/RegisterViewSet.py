from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Core.Services.Auth.Serializers import *
from Core.Services.Auth.Funciones import UsuarioFunciones

class RegisterViewSet(viewsets.ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        UsuarioFunciones.usuario_crear(**serializer.validated_data)

        return Response({"mensaje": "Usuario creado"})