from assignment.forms import SyllabusTemplateForm
from assignment.models import SyllabusTemplate
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from cal.views import create_course_entry, CalendarEntryUpdateView, CalendarEntryDeleteView


urlpatterns = patterns('course.views',
    (r'^create/$', 'create'),
    (r'^join/$', 'join'),
    (r'^(\d+)/overview/$', 'manage'),
    (r'^(\d+)/calendar/$', 'course_calendar'),
    (r'^(?P<course_id>\d+)/calendar/(?P<thisyear>\d+)/(?P<thismonth>\d+)/$', 'course_calendar'),
    (r'^(?P<course_id>\d+)/course_calendar_entry/(?P<entry_id>\d+)/$', 'course_calendar_entry_view'),
)

urlpatterns += patterns('cal.views',
    (r'^(?P<course_id>\d+)/calendar/create_course_entry/$', 'create_course_entry'),
    (r'^(?P<course_id>\d+)/calendar/update_course_entry/$', 'update_course_entry'),
    url(r'^(?P<pk>\d+)/edit/',
            login_required(
                CalendarEntryUpdateView.as_view(
                    form_class=SyllabusTemplateForm,
                    model=SyllabusTemplate,
                    template_name='course_calendar_entry_update.html',
                    success_url='/library/catalog/')), name='calendar_entry_edit'),
    (r'^(?P<pk>\d+)/delete/',
            login_required(
                CalendarEntryDeleteView.as_view(
                    model=SyllabusTemplate,
                    success_url='/library/catalog/'))),
)
