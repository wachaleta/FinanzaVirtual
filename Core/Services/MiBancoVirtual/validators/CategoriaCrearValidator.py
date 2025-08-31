from ....Application.Behaviours import Validator
from ..models import Categoria

class CategoriaCrearValidator(Validator):
    model = Categoria

    def SetRules(self):
        self.NewField("Nombre").NotEmpty().ValidateDuplicatedData()