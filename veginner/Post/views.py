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
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.
def community(req):
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
        form = PostForm()
        sort = req.GET.get('sort', '')# sorting
        order = req.GET.get('order', '')# ordering
        page = req.GET.get('page', '')# pagination
        post_value = Post.objects.values('post_id', 'writer__nickname', 'food_name', 'post_vegan_type__vegan_type', 'date', 'image', 'content')
        posts = post_value.order_by('-write_time')# default posts
        vegan_type_dict = dict()
        for obj in Vegan_type.objects.all():
            vegan_type_dict[obj.vegan_type] = obj.vegan_id
#         order_by_dict = {'Recent': '-write_time', 'Likes': '-like_count', '-write_time'}
        if sort != '' and order != '':
            if order == 'Likes':
                posts = post_value.annotate(like_count=Count('like')).order_by('-like_count','-write_time')
            else:
                posts = post_value.filter(post_vegan_type=vegan_type_dict[sort]).order_by('-write_time')
        elif sort != '' and order == '':
            posts = post_value.filter(post_vegan_type=vegan_type_dict[sort]).order_by('-write_time')
        elif sort == '' and order != '':
            if order == 'Likes':
                posts = post_value.annotate(like_count=Count('like')).order_by('-like_count','-write_time')
            else:
                posts = post_value.order_by('-write_time')
        print(posts)
        paginator = Paginator(posts, 12)
        post_list = paginator.get_page(page)
        context = {
            "post": post_list,
            "form": form
        }
        return render(req, 'Post/community.html', context)

def posting(req):
    form = PostForm()
    form.save()
    sweetify.info(req, "성공적으로 보내졌습니다.", timer=1200)
    return redirect("community")

def about(req):
    return render(req, 'Post/about.html')

def detail(req,post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(req, 'Post/detail.html', {'post': post_detail})

def delete(req,post_id):
    selected_post = Post.objects.get(post_id=post_id)
    selected_post.delete()
    return redirect("community")

def update(req,post_id):
    update_post = Post.objects.get(post_id = post_id)
    if req.method == "POST":
        update_post.date = req.POST['date']
        update_post.food_name = req.POST['food_name']
        update_post.content = req.POST["content"]
        update_post.post_vegan_type = Vegan_type.objects.get(vegan_type=req.POST["post_vegan_type"])
        update_post.save()
        return redirect('detail',post_id)

    else:
        update_postForm = PostForm
        return render(req, 'Post/detail.html', {'form':update_postForm})