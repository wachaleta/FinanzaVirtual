from ....Application.Behaviours import Validator
from ..models import Perfil

class PerfilEditarCommandHandler:
    def execute(self, command):

        PerfilEditarValidator(command)

        perfil = Perfil.objects.filter(IdPerfil = command.IdPerfil).first()

        perfil.Nombre = command.Nombre
        perfil.AgregarTotal = command.AgregarTotal

        perfil.save()

        return {
            'Id': perfil.IdPerfil
        }

class PerfilEditarValidator(Validator):
    model = Perfil

    def __init__(self, command):

        self.NewField("Nombre", command.Nombre).NotEmpty().ValidateDuplicatedDataExceptPk(command.IdPerfil)
        super().__init__()