# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView

def index(req):
    context = { 'mainHeaderBGColor' : 'main-header', 'mainHeaderFontColor' : 'main-header-font', 'isMain': True } # main page's header bg-color: green color
    return render(req, 'main.html', context)

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')