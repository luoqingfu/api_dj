from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from use_api.models import Api
from use_api.serializers import ApiSerializers


class Api_view(APIView):

    @api_view(['GET', 'POST'])
    def api_list(request):
        if request.method == 'GET':
            api = Api.objects.all()
            api_serializer = ApiSerializers(api, many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '获取成功',
                'list': api_serializer.data
            })

        if request.method == 'POST':
            api_serializers = ApiSerializers(data=request.data)
            if api_serializers.is_valid():
                api_serializers.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    'msg': '修改成功',
                    'data': api_serializers.data
                })
            return Response(api_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def api_detail(request, pk):
        try:
            api_detail = Api.objects.get(pk=pk)
        except Api.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
            api_detail = ApiSerializers(api_detail)
            return Response({
                'status': status.HTTP_200_OK,
                'data': api_detail.data
            })

    @api_view(['DELETE'])
    def api_delete(request, pk):
        try:
            api = Api.objects.get(pk=pk)
        except Api.DoesNotExist:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'msg': '不存在该条记录'
            })
        if request.method == 'DELETE':
            api.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'msg': '删除成功'
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': '删除失败'
        })


