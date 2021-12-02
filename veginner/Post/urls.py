from . import views
from django.urls import path

urlpatterns = [
    path('about', views.about, name='about'),
    path('community', views.community, name='community'),
    path('posting', views.posting, name='posting'),
]
