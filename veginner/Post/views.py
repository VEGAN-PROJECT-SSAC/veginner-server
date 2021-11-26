# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from .models import Vegan_type, Post
from User.models import User
from .forms import PostForm
import sweetify
import datetime

# Create your views here.
def community(req):
    print(req.session.session_key)
    print(req.session.get(req.session.session_key))
    v_type = [1, 2, 3, 4]
    sv_type = [5, 6, 7]
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
        return redirect("community")
    else:
        form = PostForm()
        context = {
            "vegan": vegan,
            "semi": semi_vegan,
            "form": form
        }
        return render(req, 'Post/community.html', context)
#     post = Post.objects.filter(post_vegan_type="Vegan")

def posting(req):
    form = PostForm()
#     req.POST.get()
    form.save()
    sweetify.info(req, "성공적으로 보내졌습니다.", timer=1200)
    return redirect("community")
def about(req):
    return render(req, 'Post/about.html')