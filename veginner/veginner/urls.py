"""veginner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from User.views import CustomPasswordChangeView

urlpatterns = [
    # admin
    url('^admin/', admin.site.urls),
    # user app
    path('', include('User.urls')),
    # allauth.
    path(
        'email-confirmation-done/',
        TemplateView.as_view(template_name='account.email_confirmation_done.html'),
        name='account_email_confirmation_done'
    ),
    path(
        'password/change/',
        CustomPasswordChangeView.as_view(),
        name='account_password_change'
    ),
    path('', include('allauth.urls')),
    ]

# django 기본 제공 템플릿 view를 사용하면 따로 views.py에서 정의 안 ㅎ해 줘도 되어서 걍 렌더링만 해 줄 거라
# 그냥 템플릿 뷰로 썼습니다 26번 라인