from django.db import models
class Api(models.Model):
    """
    接口表
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='接口名称', max_length=30)
    api = models.CharField(verbose_name='接口', max_length=300)
    method = models.CharField(verbose_name='请求方法', max_length=10)
    intro = models.CharField(verbose_name='接口简介', max_length=300, default='这个人很懒，不想写简介')
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'api'
        verbose_name = '接口'
        verbose_name_plural = verbose_name

    objects = models.Manager()