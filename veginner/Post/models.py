# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField
from User.models import User


# Create your models here.
class Vegan_type(models.Model):
    vegan_id = models.AutoField(primary_key=True)
    vegan_type = models.CharField(max_length=20, verbose_name='비건 타입', null=False)
    VEGAN_SORT_CHOICES = [
        ("V", "Vegetarian"),
        ("SV", "Semi_Vegetarian")
    ]
    vegan_sort = models.CharField(max_length=2, choices=VEGAN_SORT_CHOICES)
    def __str__(self):
        return str(self.vegan_type) + ' ' + str(self.vegan_id)
    class Meta:
        db_table = 'Vegan_type'
        verbose_name = '비건 타입'
        verbose_name_plural = '비건 타입'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    date = models.DateField(default=datetime.date.today, verbose_name='작성 날짜')
    food_name = models.CharField(max_length=50, verbose_name='음식 이름', null=False)
    post_vegan_type = models.ForeignKey(Vegan_type, on_delete=models.CASCADE, verbose_name='비건 종류', null=False)
    image = models.ImageField(null=False, verbose_name='음식 사진', upload_to='')
    content = TextField(verbose_name='내용')
    write_time = models.DateTimeField(auto_now=True, verbose_name="작성 시간")
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    @property
    def like_count(self):
        return self.like.count() # like 컬럼의 값의 갯수를 센다
    def __str__(self):
        return str(self.post_id) + ' ' + str(self.writer)
    class Meta:
        db_table = 'Post'
        verbose_name = '포스트'
        verbose_name_plural = '포스트'