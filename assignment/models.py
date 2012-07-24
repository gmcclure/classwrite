from django.contrib.auth.models import User
from django.db import models
from course.models import Course


class AssignmentTemplate(models.Model):
    author = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Assignment Templates"

    def __unicode__(self):
        return self.name


class Assignment(models.Model):
    course = models.ForeignKey(Course)
    created_from = models.ForeignKey(AssignmentTemplate)
    author = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.template.name


class SyllabusTemplate(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Syllabus Templates"

    def __unicode__(self):
        return self.title


class Syllabus(models.Model):
    course_id = models.ForeignKey(Course)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Syllabi"

    def __unicode__(self):
        return self.title
