from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import APIException
from rest_framework import status

class IniciarSesionCommandHandler:
    def execute(self, command):
        username = command.username
        password = command.password

        user = authenticate(username=username, password=password)

        if not user:
            raise AuthenticationError("Credenciales inválidas. Inténtelo de nuevo", status_code=401)
            # raise AuthenticationError()
        if not user.is_active:
            raise AuthenticationError("Usuario inactivo. Contacta con el administrador", status_code=403)

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class AuthenticationError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Ocurrió un error de autenticación'
    default_code = 'AuthError'

    def __init__(self, detail=None, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        
        super().__init__(detail, self.default_code)