from django.conf.urls.defaults import *
from assignment.assignment_views import AssignmentTemplateUpdateView, AssignmentTemplateDeleteView

urlpatterns = patterns('',
    (r'^create/', 'assignment.assignment_views.create'),
    (r'^(\d+)/preview/', 'assignment.assignment_views.preview'),
    url(r'^(?P<pk>\d+)/edit/', AssignmentTemplateUpdateView.as_view(), name='assignment_edit'),
    (r'^(?P<pk>\d+)/delete/', AssignmentTemplateDeleteView.as_view()),
)
