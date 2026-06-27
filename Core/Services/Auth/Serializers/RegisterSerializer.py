from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_again = serializers.CharField()

    def validate_username(self, value):
        repetido = User.objects.filter(username=value).exists()

        if repetido:
            raise ValidationError("Ya existe un usuario con ese nombre")
        
        return value

    def validate_password_again(self, value):
        password = self.initial_data.get('password')

        if value != password:
            raise ValidationError("Las contraseñas no coinciden")

        return value