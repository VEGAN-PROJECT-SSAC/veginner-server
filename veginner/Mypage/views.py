# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, Q
from django.shortcuts import render
from User.models import User
from Post.models import Vegan_type, Post


# Create your views here.
def myinfo(req):
    return render(req, 'Mypage/myinfo.html')

def myposting(req):
    return render(req, 'Mypage/myposting.html')

def monthlyreport(req):
    print(' chart go chart go !')
    dataset = Vegan_type.objects \
    .values('vegan_sort') \
    .annotate(Vegetarian_count=Count('vegan_sort'),
     Semi_Vegetarian_count=Count('vegan_sort')).order_by('vegan_sort')
#     dataset = Post.objects \
#         .values(User.objects.get()'vegan_type') \
#         .annotate(Vegan_count=Count('vegan_type'), Lacto_count=Count('vegan_type.Lacto'), Ovo_count=Count('vegan_type.Ovo'), Lacto_Ovo_count=Count('vegan_type.Lacto-Ovo'),Pesco_count=Count('vegan_type.Pesco'),Pollo_count=Count('vegan_type.Pollo'),
#         Flexitarian_count=Count('vegan_type.Flexitarian')).order_by('vegan_type')
    print(Vegan_type)
    print(Vegan_type.objects.values('vegan_type'))
    print('쿼리셋 생김')
    return render(req, 'Mypage/monthlyreport.html', {'dataset': dataset})