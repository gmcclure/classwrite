from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView
from assignment.forms import AssignmentTemplateForm
from assignment.models import AssignmentTemplate


@login_required
def create(request):
    if request.method == 'POST':
        form = AssignmentTemplateForm(request.POST)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.author = request.user
            new_assignment.full_clean()
            new_assignment.save()
            return HttpResponseRedirect('/library/catalog/')
    else:
        form = AssignmentTemplateForm()

    return render_to_response('assignmenttemplate_create.html',
            { 'form': form, },
            context_instance=RequestContext(request))


class AssignmentTemplateUpdateView(UpdateView):
    form_class=AssignmentTemplateForm
    model=AssignmentTemplate
    template_name='assignmenttemplate_update.html'
    success_url='/library/catalog/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AssignmentTemplateUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        assignment = super(AssignmentTemplateUpdateView, self).get_object()
        if not assignment.author == self.request.user:
            raise Http404
        return assignment


class AssignmentTemplateDeleteView(DeleteView):
    model=AssignmentTemplate
    success_url='/library/catalog/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AssignmentTemplateDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        assignment = super(AssignmentTemplateDeleteView, self).get_object()
        if not assignment.author == self.request.user:
            raise Http404
        return assignment


@login_required
def preview(request, assignment_id):
    assignment = get_object_or_404(AssignmentTemplate, id=assignment_id)
    if request.user.id == assignment.author_id:
        return render_to_response('assignmenttemplate_preview.html',
                { 'assignment': assignment, },
                context_instance=RequestContext(request))
