from rest_framework import serializers

from Core.Services.catalogos import models

class EfectivoMonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EfectivoMoneda
        exclude = ()