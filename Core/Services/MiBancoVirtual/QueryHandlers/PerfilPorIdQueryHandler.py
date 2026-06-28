from ..models import Perfil

class PerfilPorIdQueryHandler:
    def execute(self, command):
        perfil = Perfil.objects.first(id=command.id)

        return perfil