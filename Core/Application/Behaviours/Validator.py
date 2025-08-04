from ..Exceptions import FieldsException

class Validator:
    error_list = {}
    model = None
    command = None

    def __init__(self):
        self.Run()

    def AddError(self, field_name, message):
        self.error_list[field_name].append(message)
    
    def NewField(self, field_name, value):
        instance = self.Validate(self, field_name, value)

        return instance
    
    def AnyErrors(self):
        for i in self.error_list:
            if self.error_list[i]:
                return True
        
        return False
    
    def Run(self):
        if self.AnyErrors():
            raise FieldsException(self.error_list)

    class Validate:
        
        def __init__(self, outer, field_name, value):
            self.outer = outer
            self.field_name = field_name
            self.value = value

            self.outer.error_list[self.field_name] = []


        def AddError(self, message="Ocurrió un error", validation=True):
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

            query = {f"{self.field_name}__iexact": self.value}
            validation = self.outer.model.objects.filter(**query).exists()

            return self.AddError("Ya existe un registro con ese valor", validation)


        def ValidateDuplicatedDataExceptPk(self, Pk):

            query = {f"{self.field_name}__iexact": self.value}
            validation = self.outer.model.objects.filter(**query).exclude(pk=Pk).exists()
            print("pk")
            print(Pk)
            print(self.outer.model.objects.filter(pk=Pk))

            return self.AddError("Ya existe un registro con ese valor", validation)


        def MinimumLength(self, length):
            validation = len(self.value) < length
            return self.AddError(f"Debe de tener mínimo {length} caracteres", validation)
