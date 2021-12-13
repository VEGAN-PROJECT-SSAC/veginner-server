# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import calendar
from datetime import datetime, timedelta, date

from django.db.models import Count, Q
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.sessions.models import Session
from django.utils.safestring import mark_safe
from django.views.generic import DeleteView
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.views.generic import DeleteView
from Post.models import Vegan_type, Post
from User.models import User
from Mypage.utils import Calendar
from .forms import UserChangeForm
from User.forms import CheckPasswordForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

# Create your views here.
def myinfo(req):
    mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
    user = User.objects.filter(user_id=mySession)
    if req.method == 'POST':
        form = UserChangeForm(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect('myinfo')

    else:
        form = UserChangeForm(instance=req.user)
        context = {
            'form': form
        }
        return render(req, 'Mypage/myinfo.html', context)

def withdrawal(req):
    print("ajaxajajajajaajaj")
    mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
    session_user = User.objects.get(user_id=mySession)
    session_user.delete()
    Session.objects.get(pk=req.session.session_key).delete()
    return redirect("/")
# class account_delete_view(DeleteView):
#     model = User
#     context_object_name = 'user'
#
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse('about')

# class Multiple_forms_view(MultiFormsView):
#     template_name = "Mypage/myinfo.html"
#     form_classes = {
#         'edit_info': UserChangeForm,
#         'delete_account': CheckPasswordForm
#     }
#     success_url ={
#         'edit_info': reverse('myinfo'),
#         'delete_account': reverse('about')
#     }
#     def User_Change_form_valid(self, form):
#         return pass

def myposting(req):
    mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
    posts = Post.objects.filter(writer=mySession).all().order_by('-write_time') # 내가 쓴글만

    my_posts = list()
    for my_post in posts:
        my_posts.append(my_post)
    print(my_posts)

    return render(req, 'Mypage/myposting.html', {'my_posts' : my_posts})

def monthlyreport(req):
    return render(req, 'Mypage/monthlyreport.html')

def chart_data(req):
    mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
    dataset = Post.objects \
        .values('post_vegan_type').filter(writer=mySession) \
        .annotate(Total_count=Count('post_vegan_type'))

    result = Vegan_type.objects.values('vegan_type')

    post_display_name = dict()
    for post_tuple in Vegan_type.objects.all():
        post_display_name[post_tuple.vegan_id] = post_tuple.vegan_type
    print(post_display_name)
    chart = {
        'chart': {'plotShadow': 'false', 'type': 'pie'},
        'title': {'text': 'My Report'},
        'tooltip': {'pointFormat': '<b>{point.percentage:.1f}%, {point.y}개</b>'},
        'plotOptions': {'pie': {'showInLegend': 'false'}},
        'series': [{
            'name': 'Vegan',
            'colorByPoint': 'true',
            'data': list(map(lambda row: {'name': post_display_name[row['post_vegan_type']], 'y': row['Total_count']}, dataset))
        }]
    }
    return JsonResponse(chart)

class CalendarView(generic.ListView):
#     model = Post
#     template_name = 'Mypage/calendar.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get('month', None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         return context
#
# def get_date(req_month):
#     if req_month:
#         year, month = (int(x) for x in req_month.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()
#
# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month
#
# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month



####################### 원래 얘..
    model = Post
    template_name = 'Mypage/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        user = self.request.user
        cal = Calendar(d.year, d.month, user)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

    def get(self, request, *args, **kwargs):
        myCalSession = Session.objects.get(pk=request.session.session_key).get_decoded()["_auth_user_id"]
        request.session['myCalSession'] = myCalSession
        return super().get(request, *args, **kwargs)

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
