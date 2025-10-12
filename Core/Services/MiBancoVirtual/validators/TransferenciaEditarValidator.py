from ....Application.Behaviours import Validator
from ..models import Transaccion

class TransferenciaEditarValidator(Validator):
    model = Transaccion

    def SetRules(self):
        self.NewField("Monto").GreaterThan(0)
        self.NewField("Fecha").NotEmpty()
        self.NewField("IdCategoria").NotEmpty()

        if self.data.get("TransferenciaEntrePerfiles") == True:
            self.NewField("IdPerfilOrdenante").NotEmpty()
            self.NewField("IdPerfilBeneficiario").NotEmpty()

        else:
            self.NewField("IdCuentaOrdenante").NotEmpty()
            self.NewField("IdCuentaBeneficiaria").NotEmpty()