from ....Application.Behaviours import Validator
from ..models import Transaccion

class GastoEditarValidator(Validator):
    model = Transaccion

    def SetRules(self):
        self.NewField("Monto").GreaterThan(0)
        self.NewField("Fecha").NotEmpty()
        self.NewField("IdCategoria").NotEmpty()
        self.NewField("cuenta_ordenante").NotEmpty()
        self.NewField("perfil_ordenante").NotEmpty()