# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView

# Create your views here.
def index(req):
    return render(req, 'index.html')

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')