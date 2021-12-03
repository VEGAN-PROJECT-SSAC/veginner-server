from datetime import datetime
from calendar import HTMLCalendar
from Post.models import Post
from . import views

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, Post):
		events_per_day = Post.objects.filter(write_time__day=day)
		d = ''
# 			문자열{변수}문자열 사용할 때 쓰는 파이썬 f-string 함수입니다
		for event in events_per_day:
			d += f'<li class="{event.post_vegan_type.vegan_type}"> {event.food_name} | {event.post_vegan_type} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, Post):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, Post)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Post.objects.filter(date__year=self.year, date__month=self.month)
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, Post)}\n'
		return cal