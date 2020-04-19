from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import status, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from use_api.models import Api
from use_api.serializers import ApiSerializers


class Apiview(APIView):
    def get(self, request):
        """
        获取接口，并且根据page和pagesize分页
        :param request:
        :return:
        """
        try:
            page_size = int(request.GET.get('pageSize'))
            page = int(request.GET.get('page'))
        except (TypeError, ValueError):
            return Response({
                'code': 999,
                'msg': 'page and page_size must be integer!'
            })
        api = Api.objects.all().order_by('id')
        paginator = Paginator(api, page_size)  # paginator对象
        total = paginator.num_pages  # 总页数
        try:
            cur_page = paginator.page(page)
        except PageNotAnInteger:
            cur_page = paginator.page(1)
        except EmptyPage:
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '该页没有数据哦！！',
                'page': page,
                'pageSize': page_size,
                'totalPage': total
            })
        api_serializer = ApiSerializers(cur_page, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'msg': '获取列表成功',
            'data': api_serializer.data,
            'page': page,
            'pageSize': page_size,
            'totalPage': total

        })

    def post(self, request):
        """
        创建一个新的接口
        :param request:
        :return:
        """
        api_serializers = ApiSerializers(data=request.data)
        if api_serializers.is_valid():
            api_serializers.save()
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '添加成功',
                'data': api_serializers.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'msg': '发送未知错误'
            })


class Search(APIView):
    """
    搜索接口
    :return:
    """
    # drf 自带的搜索过滤
    # class searchApi(generics.ListAPIView):
    #     queryset = Api.objects.all()
    #     serializer_class = ApiSerializers
    #     filter_backends = (filters.SearchFilter,)
    #     search_fields = ('name', 'api')
    def get(self, request):
        pagesize = request.GET.get('pageSize', 20)
        page = request.GET.get('page', 1)
        try:
            name = request.GET.get('name')
            print(name)
            api = Api.objects.filter(name__contains=name).order_by('id')
        except ObjectDoesNotExist:
            return Response({
                'code': 999,
                'msg': '该条接口不存在'
            })
        # 获取Paginator对象
        page_api = Paginator(api, pagesize)
        # 获取总页数
        total_page = page_api.num_pages
        # 获取当前页匹配的对象
        page_api = page_api.page(page)
        # 序列化数据
        api = ApiSerializers(page_api, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'msg': '获取接口成功',
            'data': api.data,
            'page': page,
            'pageSize': pagesize,
            'totalPage': total_page
        })


class Delete(APIView):
    def post(self, request):
        """
        根据id删除对应的接口
        :param request:
        :return:
        """
        try:
            pk = request.GET.get('id')
            api = Api.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({
                'code': 999,
                'msg': '该条接口不存在'
            })
        try:
            api.delete()
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '删除成功'
            })
        except:
            return Response({
                'code': 998,
                'msg': '发送未知错误'
            })


class ApiAlter(APIView):

    def put(self, request):
        """
        根据参数修改api
        :return:
        """
        pk = request.GET.get('id')
        try:
            api = Api.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({
                'code': 999,
                'msg': '该条接口不存在'
            })
        api_obj = ApiSerializers(instance=api, data=request.data, partial=True)
        if api_obj.is_valid():
            api_obj.save()
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '修改成功',
                'data': api_obj.data
            })
        else:
            return Response({
                'code': 999,
                'msg': '修改失败'
            })