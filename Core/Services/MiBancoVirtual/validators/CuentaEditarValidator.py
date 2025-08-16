from ....Application.Behaviours import Validator
from ..models import Cuenta

class CuentaEditarValidator(Validator):
    model = Cuenta

    def SetRules(self):
        self.NewField("Nombre").NotEmpty().ValidateDuplicatedDataExceptPk(self.data["IdCuenta"])

        if self.data["EsEfectivo"] == True:
            self.NewField("BQ100").GreaterOrEqualTo(0)
            self.NewField("BQ50").GreaterOrEqualTo(0)
            self.NewField("BQ20").GreaterOrEqualTo(0)
            self.NewField("BQ10").GreaterOrEqualTo(0)
            self.NewField("BQ5").GreaterOrEqualTo(0)
            self.NewField("M100c").GreaterOrEqualTo(0)
            self.NewField("M50c").GreaterOrEqualTo(0)
            self.NewField("M25c").GreaterOrEqualTo(0)
            self.NewField("M10c").GreaterOrEqualTo(0)
            self.NewField("M5c").GreaterOrEqualTo(0)
        
        else:
            self.NewField("SaldoReal").GreaterOrEqualTo(0)