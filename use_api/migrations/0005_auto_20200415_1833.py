# Generated by Django 2.0 on 2020-04-15 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('use_api', '0004_auto_20200415_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertoken',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='api',
            options={'ordering': ('name',), 'verbose_name': '接口', 'verbose_name_plural': '接口'},
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.DeleteModel(
            name='UserToken',
        ),
    ]
