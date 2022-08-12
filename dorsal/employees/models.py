from django.db import models
from django.contrib.auth.models import User
from wagtail.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=30)
    grade = models.IntegerField()
    gender = models.CharField(max_length=15)
    nickname = models.CharField(max_length=20)
    bio = RichTextField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

