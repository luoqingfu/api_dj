from django.contrib import admin

# Register your models here.
from use_api.models import Api

admin.site.register(Api)

class Api(admin.ModelAdmin):
    search_fields = ('name')