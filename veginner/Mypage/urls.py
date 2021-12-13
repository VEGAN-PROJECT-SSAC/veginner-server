from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('mypage/myinfo', views.myinfo, name='myinfo'),
    path('mypage/myposting', views.myposting, name='myposting'),
    path('mypage/calendar/', views.CalendarView.as_view(), name='calendar'),
    path('mypage/monthlyreport', views.monthlyreport, name='monthlyreport'),
    path('mypage/monthlyreport/data/', views.chart_data, name='chart_data'),
    path('mypage/myinfo/userdelete/<int:pk>',  views.account_delete_view, name='account_delete'),
#     path('mypage/monthlyreport/test/', views.chart_test, name='chart_test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)