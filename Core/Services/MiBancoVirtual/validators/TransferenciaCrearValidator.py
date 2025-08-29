from ....Application.Behaviours import Validator
from ..models import Transaccion

class TransferenciaCrearValidator(Validator):
    model = Transaccion

    def SetRules(self):
        self.NewField("Monto").GreaterThan(0)
        self.NewField("Fecha").NotEmpty()
        self.NewField("IdCategoria").NotEmpty()

        print("TransferenciaEntrePerfiles")
        print(self.data)
        if self.data.get("TransferenciaEntrePerfiles") == True:
            self.NewField("IdPerfilOrdenante").NotEmpty()
            self.NewField("IdPerfilBeneficiario").NotEmpty()

        else:
            self.NewField("IdCuentaOrdenante").NotEmpty()
            self.NewField("IdCuentaBeneficiaria").NotEmpty()