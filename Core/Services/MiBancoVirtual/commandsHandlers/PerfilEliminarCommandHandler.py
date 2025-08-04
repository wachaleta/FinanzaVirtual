from ..models import Perfil

class PerfilEliminarCommandHandler:
    def execute(self, command):

        Perfil.objects.delete(IdPerfil=command.IdPerfil)
