from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from course.models import Course


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    classes = models.ManyToManyField(Course, through='Student')


class Student(models.Model):
    profile = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Course)
    date_joined = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    return UserProfile.objects.get_or_create(user=kwargs['instance'])
