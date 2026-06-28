from rest_framework.response import Response

from ..models import Perfil

class PerfilesQueryHandler:
    def handle(self, command):
        perfiles = Perfil.objects.filter(usuario=command.IdUsuario)

        return Response(
            {
                'data': list(perfiles)
            }
        )