from ....Application.Behaviours import Validator
from ..models import Transaccion

class IngresoCrearValidator(Validator):
    model = Transaccion

    def SetRules(self):
        self.NewField("Monto").GreaterThan(0)
        self.NewField("Fecha").NotEmpty()
        self.NewField("IdCategoria").NotEmpty()
        self.NewField("IdCuentaBeneficiaria").WithFieldName("IdCuentaOrdenante").NotEmpty()
        self.NewField("IdPerfilBeneficiario").WithFieldName("IdPerfilOrdenante").NotEmpty()