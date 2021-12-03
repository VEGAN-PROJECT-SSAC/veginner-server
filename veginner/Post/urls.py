from . import views
from django.urls import path

urlpatterns = [
    path('about', views.about, name='about'),
    path('community', views.community, name='community'),
    path('community/detail/', views.detail, name='detail'),
    path('posting', views.posting, name='posting'),
]
