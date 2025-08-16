from ....Application.Behaviours import Validator
from ..models import Perfil

class PerfilEditarValidator(Validator):
    model = Perfil

    def SetRules(self):

        self.NewField("Nombre").NotEmpty().ValidateDuplicatedDataExceptPk(self.data["IdPerfil"])