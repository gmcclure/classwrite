from django import forms
from django.forms import ModelForm, Textarea
from assignment.models import AssignmentTemplate, SyllabusTemplate
from markdown import markdown


class AssignmentTemplateForm(ModelForm):
    class Meta:
        model = AssignmentTemplate
        exclude = ('author',)
        widgets = {
            'objectives': Textarea(attrs={'cols': 30, 'rows': 20}),
            'prompt'    : Textarea(attrs={'cols': 30, 'rows': 20}),
            'rubric'    : Textarea(attrs={'cols': 30, 'rows': 20}),
        }


class SyllabusTemplateForm(ModelForm):
    class Meta:
        model = SyllabusTemplate
        exclude = ('author',)
        widgets = {
            'text'      : Textarea(attrs={'cols': 30, 'rows': 20}),
        }
