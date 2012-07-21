from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from assignment.forms import SyllabusTemplateForm
from assignment.models import SyllabusTemplate
from assignment.syllabus_views import SyllabusTemplateUpdateView, SyllabusTemplateDeleteView

urlpatterns = patterns('',
    (r'^create/', 'assignment.syllabus_views.create'),
    (r'^(\d+)/preview/', 'assignment.syllabus_views.preview'),
    url(r'^(?P<pk>\d+)/edit/',
            login_required(
                SyllabusTemplateUpdateView.as_view(
                    form_class=SyllabusTemplateForm,
                    model=SyllabusTemplate,
                    template_name='syllabustemplate_update.html',
                    success_url='/library/catalog/')), name='syllabus_edit'),
    (r'^(?P<pk>\d+)/delete/',
            login_required(
                SyllabusTemplateDeleteView.as_view(
                    model=SyllabusTemplate,
                    success_url='/library/catalog/'))),
)
