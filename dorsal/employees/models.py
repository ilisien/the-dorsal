from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=30)
    grade = models.IntegerField()
    gender = models.TextField(max_length=15)
    nickname = models.TextField(max_length=20)
    bio = RichTextField()

