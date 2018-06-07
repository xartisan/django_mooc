import datetime

from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=64, verbose_name='课程名称')
    desc = models.CharField(max_length=512, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    level = models.CharField(
        choices=(('beginner', '初级'), ('intermediate', '中级'), ('advanced', '高级')), max_length=16)
    duration = models.IntegerField(default=0, verbose_name='课程时长')
    num_students = models.IntegerField(default=0, verbose_name='学习人数')
    num_likes = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面')
    num_clicks = models.IntegerField(default=0, verbose_name='点击数')
    created_at = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='所属课程')
    name = models.CharField(max_length=128, verbose_name='章节名')
    created_at = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    name = models.CharField(max_length=128, verbose_name='视频名')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='所属章节')
    created_at = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    name = models.CharField(max_length=128, verbose_name='资源名')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='所属课程')
    url = models.FileField(upload_to='courses/resources/%Y/%m', verbose_name='资源文件')
    created_at = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
