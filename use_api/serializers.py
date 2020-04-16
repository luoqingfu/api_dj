from rest_framework import serializers
from use_api.models import Api


class ApiSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Api
        fields = (
            'id',
            'name',
            'api',
            'api_method',
            'api_intro',
            'created'
        )