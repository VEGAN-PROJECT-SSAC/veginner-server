from . import views
from django.urls import path
import django.views.defaults

urlpatterns = [
    path('about', views.about, name='about'),
    path('community', views.community, name='community'),
#     path('community/detail/', views.detail, name='detail'),
    path('community/detail/<int:post_id>/', views.detail, name='detail'),
    path('community/update/<int:post_id>/', views.update, name='update'),
    path('community/delete/<int:post_id>/', views.delete, name='delete'),
    path('ajaxlike', views.ajaxlike, name='ajaxlike'),
#     path('404', django.views.defaults.page_not_found),
]
