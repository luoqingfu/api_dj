from django.db import models


HTTP_CHOICE = (
    ('HTTP', 'HTTP'),
    ('HTTPS', 'HTTPS')
)
class Project(models.Model):
    """
    项目列表
    """
    PROJECT_CHOICES = (
        ('APP', 'APP'),
        ('WEB', 'WEB')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='项目名称', max_length=30)
    versions = models.CharField(verbose_name='项目版本', max_length=30)
    form = models.CharField(choices=PROJECT_CHOICES, verbose_name='项目类型', max_length=30)
    description = models.CharField(verbose_name='项目描述', max_length=30, default='这个人很懒不想写描述')
    last_time = models.DateTimeField(verbose_name='最后修改时间', auto_now_add=True)
    status = models.BooleanField(verbose_name='状态', default=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    objects = models.Manager()


class ApiGroup(models.Model):
    """
    接口分组
    """
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    name = models.CharField(max_length=50, verbose_name='分组名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apigroup'
        verbose_name = '接口分组'
        verbose_name_plural = '接口分组'


class Api(models.Model):
    """
    接口表
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='接口名称', max_length=30)
    api = models.CharField(verbose_name='接口', max_length=300)
    method = models.CharField(verbose_name='请求方法', max_length=10)
    intro = models.CharField(verbose_name='接口简介', max_length=300, default='这个人很懒，不想写简介')
    project = models.ForeignKey(Project, related_name='api_project', on_delete=models.CASCADE,
                                verbose_name='所属项目')
    group = models.ForeignKey(ApiGroup, related_name='api_group', blank=True, null=True,
                              on_delete=models.SET_NULL, verbose_name='所属分组')
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    httpType = models.CharField(max_length=50, default='HTTP', verbose_name='http/https', choices=HTTP_CHOICE)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'api'
        verbose_name = '接口'
        verbose_name_plural = verbose_name

    objects = models.Manager()