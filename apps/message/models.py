from django.db import models


# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名', help_text='用户名')
    email = models.EmailField(verbose_name='邮箱', help_text='邮箱')
    address = models.CharField(max_length=100, verbose_name='联系地址')
    content = models.CharField(max_length=500, verbose_name='留言内容')

    class Meta:
        verbose_name = '用户留言信息'
        verbose_name_plural = verbose_name
