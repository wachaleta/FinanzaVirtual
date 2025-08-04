from ....Application.Behaviours import Validator
from ..models import Perfil

class PerfilCrearCommandHandler:
    def handle(self, command):
        
        PerfilCrearValidator(command)

        Perfil.objects.create(
            Nombre = command.Nombre,
            AgregarTotal = command.AgregarTotal,
            IdUsuario = command.IdUsuario,
        )

class PerfilCrearValidator(Validator):
    model = Perfil

    def __init__(self, command):
        self.NewField("Nombre", command.Nombre).NotEmpty().ValidateDuplicatedData()

        super().__init__()