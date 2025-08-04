from rest_framework import serializers
from django.contrib.auth.models import User

class IniciarSesionSerializer(serializers.Serializer):
    username = serializers.CharField(
        # error_messages={
        #     'invalid': 'El correo electrónico es inválido',
        #     'blank': 'El correo no debe de estar vacío',
        #     'required': 'El correo es requerido',
        # }
    )

    password = serializers.CharField(
        write_only = True,
        # error_messages = {
        #     'blank', 'La contraseña no debe de estar vacía'
        # }
    )

    class Meta:
        model = User
        fields = ('username', 'password')