from django import forms
from django.forms import ModelForm, Textarea
from course.models import Course
from util.common import class_id_converter


class PartialCourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ('instructor',)
        widgets = { 'description': Textarea(attrs={'cols': 30, 'rows': 20}), }


class JoinCourseForm(forms.Form):
    class_id = forms.CharField(max_length=12, required=True)
    class_password = forms.CharField(max_length=12, required=True)

    def clean_class_id(self):
        cid = self.cleaned_data['class_id'].upper()

        if not cid.isalnum(): raise forms.ValidationError('The class ID should have letters and numbers only.')

        try:
            Course.objects.get(pk=class_id_converter.to_num(cid))
        except Course.DoesNotExist:
            raise forms.ValidationError('There is no class with this ID. Double-check your value.')

        return self.cleaned_data['class_id']

    def clean_class_password(self):
        if 'class_id' in self.cleaned_data:
            cid = self.cleaned_data['class_id'].upper()
            course = Course.objects.get(pk=class_id_converter.to_num(cid))

            if course.password != self.cleaned_data['class_password']:
                raise forms.ValidationError('Password is incorrect.')

        return self.cleaned_data['class_password']
