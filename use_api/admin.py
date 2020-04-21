from django.contrib import admin

# Register your models here.
from use_api.models import Api, Project, ApiGroup

admin.site.register(Api)
admin.site.register(Project)
admin.site.register(ApiGroup)