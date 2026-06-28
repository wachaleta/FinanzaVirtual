from ....Application.Behaviours import Validator
from ..models import Transaccion

class TransferenciaCrearValidator(Validator):
    model = Transaccion

    def SetRules(self):
        self.NewField("Monto").GreaterThan(0)
        self.NewField("Fecha").NotEmpty()
        self.NewField("IdCategoria").NotEmpty()

        if self.data.get("transferencia_entre_perfiles") == True:
            self.NewField("perfil_ordenante").NotEmpty()
            self.NewField("perfil_beneficiario").NotEmpty()

        else:
            self.NewField("cuenta_ordenante").NotEmpty()
            self.NewField("cuenta_beneficiaria").NotEmpty()