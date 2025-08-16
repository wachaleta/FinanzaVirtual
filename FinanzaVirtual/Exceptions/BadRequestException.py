from rest_framework import status
from rest_framework.exceptions import APIException

class BadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Ha ocurrido un error en la solicitud"
    default_code = "Error 400"

    def __init__(self, detail=None):
        if detail is not None:
            self.default_detail = detail

        super().__init__(self.default_detail, self.default_code)