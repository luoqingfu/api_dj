from django.urls import path

from use_api.api.Api import Apiview, Search, Delete, ApiAlter
from use_api.api.Project import ProjectView

urlpatterns = [
    path('apilist/', Apiview.as_view()),
    path('search/', Search.as_view()),
    path('delete/', Delete.as_view()),
    path('alter/', ApiAlter.as_view()),
    path('project/', ProjectView.as_view())
]