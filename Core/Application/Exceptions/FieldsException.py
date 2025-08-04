from rest_framework.exceptions import APIException
from rest_framework import status

class FieldsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Ha ocurrido un error en la solicitud"
    default_code = "Error 400"

    def __init__(self, detail):

        if detail is not {}:
            self.default_detail = {
                "detail": "Ha ocurrido un error de validación",
                "errores" : detail
            }

        super().__init__(self.default_detail, self.default_code)