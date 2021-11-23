from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('mypage/myinfo', views.myinfo, name='myinfo'),
    path('mypage/myposting', views.myposting, name='myposting'),
    path('mypage/monthlyreport', views.monthlyreport, name='monthlyreport'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)