from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from assignment.models import AssignmentTemplate, SyllabusTemplate

@login_required
def catalog(request):
    assignments = AssignmentTemplate.objects.filter(author=request.user)
    syllabi = SyllabusTemplate.objects.filter(author=request.user)
    return render_to_response('catalog.html',
            { 'assignments': assignments, 'syllabi': syllabi },
            context_instance=RequestContext(request))
