from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    instructor = models.ForeignKey(User)
    password = models.CharField(max_length=12)
    code = models.CharField(max_length=30)
    dept = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    section = models.CharField(max_length=20, null=True, blank=True)
    room_no = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(verify_exists=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Courses"

    def __unicode__(self):
        return ' '.join([str(self.code), self.designation])
