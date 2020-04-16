from django.db import models
class Api(models.Model):
    name = models.CharField(verbose_name='接口名称', max_length=30)
    api = models.CharField(verbose_name='接口', max_length=300)
    api_method = models.CharField(verbose_name='请求方法', max_length=10)
    api_intro = models.CharField(verbose_name='接口简介', max_length=300)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'api'
        verbose_name = '接口'
        verbose_name_plural = verbose_name
        ordering = ('name',)
