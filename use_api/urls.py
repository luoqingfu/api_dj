from django.urls import path

from use_api.api.Api import Apiview, Search, Delete, ApiAlter

urlpatterns = [
    path('apilist/', Apiview.as_view()),
    path('search/', Search.as_view()),
    path('delete/', Delete.as_view()),
    path('alter/', ApiAlter.as_view())
]