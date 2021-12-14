from datetime import datetime, timedelta
from calendar import HTMLCalendar
from Post.models import Post
from . import views
from django.db.models import Q

from django.contrib.sessions.models import Session

# class Calendar(HTMLCalendar):
#     def __init__(self, year=None, month=None, user=None):
#         self.year = year
#         self.month = month
#         super(Calendar, self).__init__()
#
#     # formats a day as a td
#     # filter events by day
#     def formatday(self, day, Posts):
#         events_per_day = Post.objects.filter(date__day=day)
#         d = ''
#         # 문자열{변수}문자열 사용할 때 쓰는 파이썬 f-string 함수입니다
#         for event in events_per_day:
#             d += f'<div class="{event.post_vegan_type.vegan_type} mx-1 calendar-li"> </div>'
#
#         if day != 0:
#             return f"<td><div class='date'>{day}</div><div class='calendar-ul px-1 d-flex flex-wrap justify-content-center'> {d} </div></td>"
#         return '<td></td>'
#
#     # formats a week as a tr
#     def formatweek(self, theweek, Posts):
#         week = ''
#         for d, weekday in theweek:
#             week += self.formatday(d, Posts)
#         return f'<tr> {week} </tr>'
#
#     # formats a month as a table
#     # filter events by year and month
#     def formatmonth(self, withyear=True):
#         Posts = Post.objects.values('post_id').filter(date__year=self.year, date__month=self.month)
#         cal = f'<table border="1" cellpadding="0" cellspacing="0" class="calendar table-bordered">\n'
#         cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
#         cal += f'{self.formatweekheader()}\n'
#         for week in self.monthdays2calendar(self.year, self.month):
#             cal += f'{self.formatweek(week, Posts)}\n'
#         return cal

############## 찐!
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, Posts):
        events_per_day = Post.objects.filter(date__day=day, date__month=self.month, date__year=self.year, writer=self.user.user_id)
        d = ''
        # 문자열{변수}문자열 사용할 때 쓰는 파이썬 f-string 함수입니다
        for event in events_per_day:
            d += f'<div class="{event.post_vegan_type.vegan_type} mx-1 calendar-li"> </div>'

        if day != 0:
            return f"<td><div><div class='date'>{day}</div><div class='calendar-ul px-1 d-flex flex-wrap justify-content-center'> {d} </div></div></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, Posts):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, Posts)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        Posts = Post.objects.values('date').filter(date__year=self.year, date__month=self.month).order_by('date')
        print("나는 포스트 필터한거",Posts)
        All = Post.objects.values('date').all().order_by('date')
        print("모두", All)
#         events = Post.objects.filter(date__year=self.year, date__month=self.month)
        cal = f'<table cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, Posts)}\n'
        return cal