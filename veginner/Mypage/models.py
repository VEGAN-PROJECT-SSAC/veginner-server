# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField
from User.models import User
from Post.models import Type, Post

# Create your models here.
class Like(models.Model):
    pass