from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import UpdateView, DeleteView
from assignment.forms import SyllabusTemplateForm
from assignment.models import Syllabus, SyllabusTemplate


@login_required
def create(request):
    if request.method == 'POST':
        form = SyllabusTemplateForm(request.POST)
        if form.is_valid():
            new_syllabus = form.save(commit=False)
            new_syllabus.author = request.user
            new_syllabus.full_clean()
            new_syllabus.save()
            return HttpResponseRedirect('/library/catalog/')
    else:
        form = SyllabusTemplateForm()

    return render_to_response('syllabustemplate_create.html',
            { 'form': form, },
            context_instance=RequestContext(request))


class SyllabusTemplateUpdateView(UpdateView):
    def get_object(self, queryset=None):
        syllabus = super(SyllabusTemplateUpdateView, self).get_object()
        if not syllabus.author == self.request.user:
            raise Http404
        return syllabus


class SyllabusTemplateDeleteView(DeleteView):
    def get_object(self, queryset=None):
        syllabus = super(SyllabusTemplateDeleteView, self).get_object()
        if not syllabus.author == self.request.user:
            raise Http404
        return syllabus


@login_required
def preview(request, assignment_id):
    syllabus = get_object_or_404(SyllabusTemplate, id=assignment_id)
    if request.user.id == syllabus.author_id:
        return render_to_response('syllabustemplate_preview.html',
                { 'syllabus': syllabus, },
                context_instance=RequestContext(request))
