# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from .models import Vegan_type, Post
from User.models import User
from .forms import PostForm
import sweetify

# Create your views here.
def community(req):
    print(req.session.session_key)
    print(req.session.get(req.session.session_key))
    vegan = Post.objects.filter(post_vegan_type=1)
    if req.method == 'POST':
        nickname=req.POST.get("username")
        print("community post 들어옴")
        form = PostForm(req.POST)
        print(form)
        if form.is_valid():
#             form.cleaned_data.get("")
            form.instance.writer = User.objects.get(nickname=nickname)

#             user = authenticate(req, writer)
            form.save()
            print("폼저장")
        else:
            form.instance.writer = User.objects.get(nickname=nickname)
            form.save()
        return redirect("community")
    else:
        form = PostForm()
        context = {
            "post": vegan,
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