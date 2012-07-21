from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from course.models import Course

def welcome(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')

    return render_to_response('welcome.html', context_instance=RequestContext(request))

@login_required
def index(request):
    instructor_classes = Course.objects.filter(instructor=request.user.id)
    student_classes = request.user.get_profile().classes
    return render_to_response('index.html',
            { 'instructor_classes': instructor_classes, 'student_classes': student_classes.all() },
            context_instance=RequestContext(request))

def logout_session(request):
    logout(request)
    return HttpResponseRedirect('/')
