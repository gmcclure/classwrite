from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

def markdown_parser(request):
    if request.method == 'POST':
        return render_to_response('markitup_preview.html',
                { 'preview': request.POST['data'] },
                context_instance=RequestContext(request))
