from rest_framework import serializers

class CuentasListRequestSerializer(serializers.Serializer):
    searchText = serializers.CharField(required=False)
    activo = serializers.BooleanField(required=False, allow_null=True, default=None)