from decimal import Decimal

from ..Exceptions import FieldsException

class Validator:
    error_list = {}
    data = {}
    model = None

    def SetData(self, data):
        self.data = data
        self.error_list = {}

    def SetRules(self):
        pass

    def AddError(self, field_name, message):
        self.error_list[field_name].append(message)
    
    def NewField(self, field_name, value = ""):
        instance = self.Validate(self, field_name, value)

        return instance
    
    def CleanEmtpyErrors(self):
        claves_a_eliminar = [clave for clave, valor in self.error_list.items() if not valor]
        for clave in claves_a_eliminar:
            del self.error_list[clave]
        return self.error_list
    
    def Run(self):
        if self.CleanEmtpyErrors():
            raise FieldsException(self.error_list)

    class Validate:
        """
        Se crea una instancia por cada cammpo a validar
        """
        
        def __init__(self, outer, field_name, value):
            self.outer = outer
            self.field_name = field_name
            self.value = self.outer.data[field_name]

            self.outer.error_list[self.field_name] = []


        def AddError(self, message="Ocurrió un error", validation=True):
            """
            Muestra un mensaje de error cuando la validación se cumple
            """
            if validation is True:
                self.outer.AddError(self.field_name, message)
            
            return self


        def NotEmpty(self):
            message = "El campo es requerido"
            
            if self.value is None:
                self.AddError(message)
            
            if self.value == "":
                self.AddError(message)
            
            return self


        def ValidateDuplicatedData(self):
            query = {
                f"{self.field_name}__iexact": self.value,
                "IdUsuario": self.outer.data["IdUsuario"]
            }

            validation = self.outer.model.objects.filter(**query).exists()

            return self.AddError("Ya existe un registro con ese valor", validation)


        def ValidateDuplicatedDataExceptPk(self, Pk):
            query = {
                f"{self.field_name}__iexact": self.value,
                "IdUsuario": self.outer.data["IdUsuario"]
            }
            validation = self.outer.model.objects.filter(**query).exclude(pk=Pk).exists()

            return self.AddError("Ya existe un registro con ese valor", validation)


        def MinimumLength(self, length):
            validation = len(self.value) < length
            return self.AddError(f"Debe de tener mínimo {length} caracteres", validation)
        

        def GreaterOrEqualTo(self, size):
            validation = Decimal(self.value) < size
            return self.AddError(f"Debe de ser mayor o igual a {size}", validation)
