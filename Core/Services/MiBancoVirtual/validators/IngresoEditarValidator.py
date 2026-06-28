from ....Application.Behaviours import Validator
from ..models import Transaccion

class IngresoEditarValidator(Validator):
    model = Transaccion

    def SetRules(self):
        self.NewField("Monto").GreaterThan(0)
        self.NewField("Fecha").NotEmpty()
        self.NewField("IdCategoria").NotEmpty()
        self.NewField("cuenta_beneficiaria").WithFieldName("cuenta_ordenante").NotEmpty()
        self.NewField("perfil_beneficiario").WithFieldName("perfil_ordenante").NotEmpty()