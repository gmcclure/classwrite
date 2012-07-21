from calendar import HTMLCalendar, month_name
from datetime import date
from django.db import models
from django.utils.html import conditional_escape as esc
from course.models import Course


class CourseCalendar(HTMLCalendar):
    def __init__(self, course_id, entry_book=None):
        super(CourseCalendar, self).__init__()
        self.course_id, self.entry_book = course_id, entry_book

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if self.entry_book and self.entry_book[day]:
                cssclass += ' filled'
                body = ['<ul>']
                for entry in self.entry_book[day]:
                    body.append('<li>')
                    body.append('<a href="%s">' % entry.get_absolute_url())
                    body.append(esc(entry.title))
                    body.append('</a><li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(CourseCalendar, self).formatmonth(year, month)

    def formatmonthname(self, theyear, themonth, withyear=True):
        reqdate = date(theyear, themonth, 1)
        month_prev = reqdate.replace(month=reqdate.month-1)
        month_next = reqdate.replace(month=reqdate.month+1)
        month_prev_url = '/course/%s/calendar/%s/%s/' % (self.course_id, month_prev.year, month_prev.month)
        month_next_url = '/course/%s/calendar/%s/%s/' % (self.course_id, month_next.year, month_next.month)
        if withyear:
            s = '<a class="month_link" href="%s">&lt;&lt;</a> %s, %s <a class="month_link" href="%s">&gt;&gt;</a>' % (month_prev_url, month_name[themonth], theyear, month_next_url)
        else:
            s = '%s' % month_name[themonth]

        return '<tr><th colspan="7" class="month">%s</th></tr>' % s


class CourseEntry(models.Model):
    course = models.ForeignKey(Course)
    dated = models.DateField()
    title = models.CharField(max_length = 100)
    text = models.TextField(max_length=50000, null=True, blank=True)

    def get_absolute_url(self):
        return '/course/%s/course_calendar_entry/%s' % (self.course.id, self.id)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"
