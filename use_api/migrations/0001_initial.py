# Generated by Django 2.1 on 2020-04-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='接口名称')),
                ('api', models.CharField(max_length=300, verbose_name='接口')),
                ('api_method', models.CharField(max_length=10, verbose_name='请求方法')),
                ('api_intro', models.CharField(max_length=300, verbose_name='接口简介')),
            ],
        ),
    ]