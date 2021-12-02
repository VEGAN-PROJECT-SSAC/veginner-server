# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, Q
from django.shortcuts import render
from User.models import User
from Post.models import Vegan_type, Post
import json



# Create your views here.
def myinfo(req):
    return render(req, 'Mypage/myinfo.html')

def myposting(req):
    return render(req, 'Mypage/myposting.html')

def monthlyreport(req):
#     print(' chart go chart go !')
# #     dataset = Vegan_type.objects \
# #     .values('vegan_sort') \
# #     .annotate(Vegetarian_count=Count('vegan_sort'),
# #      Semi_Vegetarian_count=Count('vegan_sort')).order_by('vegan_sort')
#     dataset = Post.objects \
#         .values(User.objects.get()) \
#         .annotate(Vegan_count=Count('vegan_type'), Lacto_count=Count('vegan_type.Lacto'), Ovo_count=Count('vegan_type.Ovo'), Lacto_Ovo_count=Count('vegan_type.Lacto-Ovo'),Pesco_count=Count('vegan_type.Pesco'),Pollo_count=Count('vegan_type.Pollo'),
#         Flexitarian_count=Count('vegan_type.Flexitarian')).order_by('vegan_type')
    dataset = Post.objects \
        .values('post_vegan_type') \
        .annotate(Vegan_count=Count('post_vegan_type', filter=Q(post_vegan_type=8)), Lacto_count=Count('post_vegan_type', filter=Q(post_vegan_type=9)), Ovo_count=Count('post_vegan_type', filter=Q(post_vegan_type=10)), Lacto_Ovo_count=Count('post_vegan_type', filter=Q(post_vegan_type=11)),Pesco_count=Count('post_vegan_type', filter=Q(post_vegan_type=12)),Pollo_count=Count('post_vegan_type', filter=Q(post_vegan_type=13)), Flexitarian_count=Count('post_vegan_type', filter=Q(post_vegan_type=14)))

    categories = list()
    Vegan_series = list()
    Lacto_series = list()
    Ovo_series = list()
    Lacto_Ovo_series = list()
    Pesco_series = list()
    Pollo_series = list()
    Flexitarian_series = list()

    for vegan in dataset:
        categories.append('%s Class' % vegan['post_vegan_type'])
        Vegan_series.append(vegan['Vegan_count'])
        Lacto_series.append(vegan['Lacto_count'])
        Ovo_series.append(vegan['Ovo_count'])
        Lacto_Ovo_series.append(vegan['Lacto_Ovo_count'])
        Pesco_series.append(vegan['Pesco_count'])
        Pollo_series.append(vegan['Pollo_count'])
        Flexitarian_series.append(vegan['Flexitarian_count'])

    print(Post.objects.all())
    print(Post.objects.values('food_name'))
    print(Post.objects.values('post_vegan_type'))
    print(Vegan_type.objects.values('vegan_type'))
    print('쿼리셋 생김')
    return render(req, 'Mypage/monthlyreport.html', {
        'categories': json.dumps(categories),
        'Vegan_series': json.dumps(Vegan_series),
        'Lacto_series': json.dumps(Lacto_series),
        'Ovo_series': json.dumps(Ovo_series),
        'Lacto_Ovo_series': json.dumps(Lacto_Ovo_series),
        'Pesco_series': json.dumps(Pesco_series),
        'Pollo_series': json.dumps(Pollo_series),
        'Flexitarian_series': json.dumps(Flexitarian_series),
    })