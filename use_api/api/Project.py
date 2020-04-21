#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Project.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 11:18 下午   luoqingfu   1.0         None
'''

# import lib
from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from use_api.models import Project
from use_api.serializers import ProjectSerializers


class ProjectView(APIView):
    def get(self, request):
        """
        获取项目列表
        :param request:
        :return:
        """
        try:
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('pageSize', 20))
        except (TypeError, ValueError):
            return Response({
                'code': 999,
                'msg': 'page和pagesize只能是整数'
            })
        projects = Project.objects.all().order_by('id')  # 获取project对象
        paginator = Paginator(projects, page_size)  # 获取paginator 分页对象
        total = paginator.num_pages
        try:
            curr_page = paginator.page(page)
        except EmptyPage:
            return Response({
                'code': status.HTTP_200_OK,
                'msg': '该页没有数据哦！！',
                'page': page,
                'pageSize': page_size,
                'totalPage': total
            })
        projects = ProjectSerializers(curr_page, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'msg': '获取项目列表成功',
            'data': projects.data,
            'pageSize': page_size,
            'totalPage': total
        })