from ....Application.Behaviours import Validator
from ..models import Categoria

class CategoriaEditarValidator(Validator):
    model = Categoria

    def SetRules(self):
        self.NewField("Nombre").NotEmpty().ValidateDuplicatedDataExceptPk(self.data["IdCategoria"])