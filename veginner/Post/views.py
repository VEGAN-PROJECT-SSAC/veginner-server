# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from .models import Vegan_type, Post
from .forms import PostForm

# Create your views here.
def community(req):
    print(req.session.session_key)
    vegan = Post.objects.filter(post_vegan_type=1)
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():
            form.instance.writer = self.req.user
            form.save()
        return redirect(req, "community")
    else:
        form = PostForm()
        context = {
            "post": vegan,
            "form": form
        }
        return render(req, 'Post/community.html', context)
#     post = Post.objects.filter(post_vegan_type="Vegan")

def posting(req):
    #form data save()
    return redirect(req, "community")
def about(req):
    return render(req, 'Post/about.html')