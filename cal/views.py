from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import UpdateView, DeleteView
from cal.forms import CourseEntryForm
from course.models import Course


def create_course_entry(request, course_id):
    '''Creates, for an instructor, a general calendar entry for a course calendar.'''
    if request.method == 'POST':
        form = CourseEntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.course = Course.objects.get(pk=course_id)
            new_entry.full_clean()
            new_entry.save()
            return HttpResponseRedirect('/course/%s/calendar/' % course_id)
    else:
        form = CourseEntryForm()

    return render_to_response('course_entry_create.html',
            { 'course_id': course_id, 'form': form, },
            context_instance=RequestContext(request))


def update_course_entry(request, course_id):
    pass


class CalendarEntryUpdateView(UpdateView):
    '''Updates a general calendar entry for a course calendar.'''
    def get_object(self, queryset=None):
        entry = super(CalendarEntryUpdateView, self).get_object()
        if not entry.course.instructor == self.request.user:
            raise Http404
        return entry


class CalendarEntryDeleteView(DeleteView):
    '''Deletes a course calendar entry.'''
    def get_object(self, queryset=None):
        entry = super(CalendarEntryUpdateView, self).get_object()
        if not entry.course.instructor == self.request.user:
            raise Http404
        return entry
