import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', help_text='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=(('male', '男'), ('female', '女')), default='male')
    address = models.CharField(max_length=100, default='', verbose_name='用户地址', help_text='用户地址')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# Email verification code model
class EmailVerificationCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码', help_text='验证码')
    email = models.EmailField(verbose_name='邮箱', help_text='邮箱')
    send_type = models.CharField(
        max_length=10,
        choices=(('register', '注册'), ('forget', '找回密码')),
        verbose_name='验证码类型',
        help_text='验证码类型')
    send_time = models.DateField(
        default=datetime.datetime.now, verbose_name='发送时间', help_text='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


# Banner model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', help_text='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址', help_text='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序', help_text='顺序')
    created_at = models.DateTimeField(
        default=datetime.datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '轮播图',
        verbose_name_plural = verbose_name

