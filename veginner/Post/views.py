# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Vegan_type, Post
from User.models import User
from .forms import PostForm
import sweetify
import datetime
from django.contrib.sessions.models import Session
from django.db.models import Count

# Create your views here.
def community(req):
#     print(Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"])# session에서 User pk 가져오기
    v_type = [8, 9, 10, 11]
    sv_type = [12, 13, 14]
    vegan = Post.objects.filter(post_vegan_type__in=v_type)
    semi_vegan = Post.objects.filter(post_vegan_type__in=sv_type)

    if req.method == 'POST':
#         nickname=req.POST.get("username")
        print("community post 들어옴")
#         form.instance.writer = User.objects.get(nickname=form["writer"].value)
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            post = Post()
            post.writer = User.objects.get(nickname=req.POST.get("writer"))
            post.date = form.cleaned_data["date"]
            post.food_name = form.cleaned_data["food_name"]
            post.post_vegan_type = Vegan_type.objects.get(vegan_type=form.cleaned_data["post_vegan_type"])
            post.image = form.cleaned_data["image"]
            post.content = form.cleaned_data["content"]
            post.save()
            print("폼저장")

        else:
            print("유효성 또 실패")
            sweetify.warning(req, form.non_field_errors(), timer=1200)
        return redirect('community')
    else:
        print('GET방식 들어옴')
        form = PostForm()
        sort = req.GET.get('sort', '')# sorting
        order = req.GET.get('order', '')# ordering
        page = req.GET.get('page', '')# pagination
        post = Post.objects.all().order_by('-write_time')
        # sorting
        if sort == 'All':
            post = Post.objects.all()
        if sort == 'Vegan':# 8000/community?sort=Vegan
            post = Post.objects.filter(post_vegan_type__in=v_type)
        elif sort == 'Semi_Vegan':# choice로 필터링 하는거 노가다방식, 더 좋은 방식이 있는지 모르겠어요 찾아봐야해
            post = Post.objects.filter(post_vegan_type__in = sv_type)

        # ordering
        if order == 'Recent':# 8000/community?sort=Vegan&order=Recent
            # post = Post.objects.annotate(like=Count(''))
            post = Post.objects.order_by('-write_time')
        elif order == 'Likes':
            post = Post.objects.filter(post_vegan_type=8).annotate(like_count=Count('like')).order_by('-like_count')
#             print(Post.objects.annotate(like_count=Count('like')))
#             print(Post.objects.get(post_id=1017).like.count())
#             like_count = Post.objects.order_by('-like_count')
#             print(like_count)
        elif order == 'Default':
            pass

        print(post)
        context = {
            "post": post,
            "form": form
        }
        return render(req, 'Post/community.html', context)
def posting(req):
    form = PostForm()
#     req.POST.get()
    form.save()
    sweetify.info(req, "성공적으로 보내졌습니다.", timer=1200)



    return redirect("community")
def about(req):
    return render(req, 'Post/about.html')