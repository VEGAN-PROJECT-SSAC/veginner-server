from . import views
from django.urls import path

urlpatterns = [
    path('about', views.about, name='about'),
    path('community', views.community, name='community'),
#     path('community/detail/', views.detail, name='detail'),
    path('community/detail/<int:post_id>/', views.detail, name='detail'),
    path('community/update/<int:post_id>/', views.update, name='update'),
    path('community/delete/<int:post_id>/', views.delete, name='delete'),
    path('ajaxlike', views.ajaxlike, name='ajaxlike'),
    path('posting', views.posting, name='posting'),
]
