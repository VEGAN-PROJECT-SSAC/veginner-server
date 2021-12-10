# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count
from allauth.account.views import PasswordChangeView
from Post.models import Vegan_type, Post
from Post.forms import PostForm

def index(req):
    post_value = Post.objects.values('post_id', 'writer__nickname', 'food_name', 'post_vegan_type__vegan_type', 'date', 'image', 'content').annotate(like_count=Count('like'))
    posts = post_value.order_by('-like_count')[:4]
    context = { 'mainHeaderBGColor' : 'main-header', 'mainHeaderFontColor' : 'main-header-font', 'isMain': True, 'posts': posts } # main page's header bg-color: green color
    return render(req, 'main.html', context)

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')