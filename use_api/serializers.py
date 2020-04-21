from rest_framework import serializers
from use_api.models import Api, Project


class ApiSerializers(serializers.ModelSerializer):
    """
    接口信息序列化
    """
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Api
        fields = (
            'id',
            'name',
            'api',
            'method',
            'intro',
            'httpType',
            'group_id',
            'project_id',
            'created'
        )


class ProjectSerializers(serializers.ModelSerializer):
    """
    项目信息序列化
    """
    last_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'versions',
            'form',
            'description',
            'last_time'
        )