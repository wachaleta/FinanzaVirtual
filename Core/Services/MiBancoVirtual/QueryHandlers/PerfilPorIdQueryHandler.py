from ..models import Perfil

class PerfilPorIdQueryHandler:
    def execute(self, command):
        perfil = Perfil.objects.first(IdPerfil=command.IdPerfil)

        return perfil