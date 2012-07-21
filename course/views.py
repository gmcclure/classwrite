from datetime import date
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from account.models import Student
from assignment.models import Assignment
from cal.models import CourseCalendar, CourseEntry
from course.forms import PartialCourseForm, JoinCourseForm
from course.models import Course
from util.common import class_id_converter


@login_required
def create(request):
    if request.method == 'POST':
        form = PartialCourseForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.instructor = request.user
            new_class.full_clean()
            new_class.save()
            return HttpResponseRedirect('/home/')
    else:
        form = PartialCourseForm()

    return render_to_response('create_course.html',
            { 'form': form, },
            context_instance=RequestContext(request))


@login_required
def join(request):
    if request.method == 'POST':
        form = JoinCourseForm(request.POST)
        if form.is_valid():
            cid = form.cleaned_data['class_id'].upper()
            course = Course.objects.get(pk=class_id_converter.to_num(cid))
            if course.instructor.id == request.user.id:
                messages.error(request, "You're already teaching this class!")
            else:
                new_enrollment = Student.objects.create(profile=request.user.get_profile(), course=course)
                new_enrollment.save()

            return HttpResponseRedirect('/home/')
    else:
        form = JoinCourseForm()

    return render_to_response('join.html',
            { 'form': form, },
            context_instance=RequestContext(request))


@login_required
def manage(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assignments = Assignment.objects.filter(course=course_id)
    if request.user.id == course.instructor.id:
        return render_to_response('manage_course.html',
                { 'course': course, 'course_id': class_id_converter.from_num(course.id), 'assignments': assignments, 'students': course.student_set.all() },
                context_instance=RequestContext(request))


@login_required
def create_assignment(request):
    return render_to_response('create_assignment.html',
            context_instance=RequestContext(request))


@login_required
def course_calendar(request, course_id, thisyear=date.today().year, thismonth=date.today().month):
    entries = CourseEntry.objects.filter(dated__month=thismonth, dated__year=thisyear, course=course_id)
    entry_book = dict()
    for i in range(32): entry_book[i] = []
    for entry in entries:
        entry_book[entry.dated.day].append(entry)
    calendar = CourseCalendar(course_id, entry_book)
    return render_to_response('course_calendar.html',
            { 'calendar': mark_safe(calendar.formatmonth(int(thisyear), int(thismonth))), 'course_id': course_id },
            context_instance=RequestContext(request))


@login_required
def course_calendar_entry_view(request, course_id, entry_id):
    '''View a course calendar entry.'''
    entry = CourseEntry.objects.get(pk=entry_id)
    return render_to_response('course_calendar_entry_view.html',
            { 'entry': entry },
            context_instance=RequestContext(request))
