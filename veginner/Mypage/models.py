# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField
from User.models import User
from Post.models import Vegan_type, Post

# Create your models here.
# 'Like를 Post로 옮겼기에' 여기 모델은 나중에 mypage에서 통계할 때 사용하거나 안하거나? 하면 될 것 같습니다