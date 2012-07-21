from django.forms import ModelForm, Textarea
from django.forms.extras.widgets import SelectDateWidget
from cal.models import CourseEntry

class CourseEntryForm(ModelForm):
    class Meta:
        model = CourseEntry
        exclude = ('course',)
        widgets = {
            'dated' : SelectDateWidget(),
            'text'  : Textarea(attrs={'cols' : 30, 'rows' : 20}),
        }
