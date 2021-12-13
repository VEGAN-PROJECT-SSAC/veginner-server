from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Vegan_type, Post
from User.models import User
from .forms import PostForm
import sweetify
import datetime
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.sessions.models import Session
from django.db.models import Count
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json

# Create your views here.
def community(req):
    if req.method == 'POST':
        print("community post 들어옴")
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
        post_value = Post.objects.values('post_id', 'writer__nickname', 'food_name', 'post_vegan_type__vegan_type', 'date', 'image', 'content').annotate(like_count=Count('like'))
        posts = post_value.annotate(like_count=Count('like')).order_by('-write_time')# default posts
        vegan_type_dict = dict()
        for obj in Vegan_type.objects.all():
            vegan_type_dict[obj.vegan_type] = obj.vegan_id
        if sort != '' and order != '':
            if order == 'Likes':
                posts = post_value.filter(post_vegan_type=vegan_type_dict[sort]).order_by('-like_count','-write_time')
            else:
                posts = post_value.filter(post_vegan_type=vegan_type_dict[sort]).order_by('-write_time')
        elif sort != '' and order == '':
            posts = post_value.filter(post_vegan_type=vegan_type_dict[sort]).order_by('-write_time')
        elif sort == '' and order != '':
            if order == 'Likes':
                posts = post_value.order_by('-like_count','-write_time')
            else:
                posts = post_value.order_by('-write_time')
        paginator = Paginator(posts, 12)
        post_list = paginator.get_page(page)
        mySession = req.session.session_key
        if mySession == None:
            me_like = {}
        else:
            me_like = Post.objects.values('post_id').filter(like__user_id=req.user.user_id)
        me_like_list = []
        for m in me_like:
            me_like_list.append(m['post_id'])
        context = {
            "post": post_list,
            "form": form,
            "me_like_list": me_like_list
        }
        return render(req, 'Post/community.html', context)

# 좋아요 뷰
@require_POST
@login_required
def ajaxlike(req):
    if req.method == 'POST':
        user = req.user
        posting_id = req.POST.get('pk', None)
        post = Post.objects.get(post_id=posting_id)
        print(post)
        if post.like.filter(user_id=user.user_id).exists():
            post.like.remove(user)
            message = "좋아요를 취소하였습니다"
            state = "cancel"
        else:
            post.like.add(user)
            message = "좋아요 완료"
            state = "like"
    print(state)
    context = {
        'likes_count': post.like_count,
        'message': message,
        'state': state
        }
    return JsonResponse(context)

# about 페이지
def about(req):
    return render(req, 'Post/about.html')

# 게시글 detail
def detail(req,post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(req, 'Post/detail.html', {'post': post_detail})

# 게시글 삭제
def delete(req,post_id):
    selected_post = Post.objects.get(post_id=post_id)
    if os.path.join(selected_post.image.path):
        os.remove(os.path.join(selected_post.image.path))
        selected_post.delete()
        return redirect("community")
    else:
        print("The file does not exist")
        return redirect("detail",post_id)

# 게시글 수정
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
        context = {
                'form': update_postForm,
                'post': update_post
            }
        return render(req, 'Post/detail.html', context)