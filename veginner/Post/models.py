# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField
from User.models import User


# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=20, verbose_name='비건 타입')
    def __str__(self):
        return str(self.type)
    class Meta:
        db_table = 'Type'
        verbose_name = '비건 타입'
        verbose_name_plural = '비건 타입'


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    date = models.DateField(default=datetime.date.today, verbose_name='작성 날짜')
    food_name = models.CharField(max_length=50, verbose_name='음식 이름', null=False)
    vege_type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='비건 종류', null=False)
    image = models.ImageField(null=False, verbose_name='음식 사진', upload_to='')
    content = TextField(verbose_name='내용')
    write_time = models.DateTimeField(auto_now=True, verbose_name="작성 시간")
    def __str__(self):
        return str(self.writer) + ' ' + str(self.write_time)
    class Meta:
        db_table = 'Post'
        verbose_name = '포스트'
        verbose_name_plural = '포스트'

