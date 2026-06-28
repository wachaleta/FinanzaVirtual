from ....Application.Behaviours import Validator
from ..models import Cuenta

class CuentaCrearValidator(Validator):
    model = Cuenta

    def SetRules(self):
        self.NewField("Nombre").NotEmpty().ValidateDuplicatedData()

        if self.data["es_efectivo"] == True:
            self.NewField("bQ100").GreaterOrEqualTo(0)
            self.NewField("bQ50").GreaterOrEqualTo(0)
            self.NewField("bQ20").GreaterOrEqualTo(0)
            self.NewField("bQ10").GreaterOrEqualTo(0)
            self.NewField("bQ5").GreaterOrEqualTo(0)
            self.NewField("m100c").GreaterOrEqualTo(0)
            self.NewField("m50c").GreaterOrEqualTo(0)
            self.NewField("m25c").GreaterOrEqualTo(0)
            self.NewField("m10c").GreaterOrEqualTo(0)
            self.NewField("m5c").GreaterOrEqualTo(0)
        
        else:
            self.NewField("saldo_real").GreaterOrEqualTo(0)
