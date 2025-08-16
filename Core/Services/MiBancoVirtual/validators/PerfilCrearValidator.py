from ....Application.Behaviours import Validator
from ..models import Perfil

class PerfilCrearValidator(Validator):
    model = Perfil

    def SetRules(self):
        self.NewField("Nombre").NotEmpty().ValidateDuplicatedData()