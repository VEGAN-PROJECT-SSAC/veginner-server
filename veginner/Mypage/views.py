# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from User.models import User

# Create your views here.
def myinfo(req):
    return render(req, 'Mypage/myinfo.html')

def myposting(req):
    return render(req, 'Mypage/myposting.html')

def monthlyreport(req):
    return render(req, 'Mypage/monthlyreport.html')