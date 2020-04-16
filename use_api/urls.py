from django.urls import path

from use_api.api import Api

urlpatterns = [
    path('apilist/', Api.Api_view.api_list),
    path('apidetail/<int:pk>/', Api.Api_view.api_detail),
    path('apidelete/<int:pk>/', Api.Api_view.api_delete),
]