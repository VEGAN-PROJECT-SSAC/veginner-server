# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count
from allauth.account.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from Post.models import Vegan_type, Post
from User.models import User
from Post.forms import PostForm
from User.forms import CheckPasswordForm

def index(req):
    post_value = Post.objects.values('post_id', 'writer__nickname', 'food_name', 'post_vegan_type__vegan_type', 'date', 'image', 'content').annotate(like_count=Count('like'))
    posts = post_value.order_by('-like_count')[:4]
    context = { 'mainHeaderBGColor' : 'main-header', 'mainHeaderFontColor' : 'main-header-font', 'isMain': True, 'posts': posts } # main page's header bg-color: green color
    return render(req, 'main.html', context)

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')

# @login_required
# def account_delete_view(req):
#     if req.method == 'POST':
#         password_form = CheckPasswordForm(req.user, req.POST)
#         print('유저찍히나요?',req.user)
#         if password_form.is_valid():
#             req.user.delete()
#             logout(req)
#             messages.success(req, "회원탈퇴가 완료되었습니다.")
#             return redirect('../../about')
#     else:
#         print(req.user)
#         password_form = CheckPasswordForm(req.user)
#
#     return render(req, 'account/login.html', {'password_form':password_form})

