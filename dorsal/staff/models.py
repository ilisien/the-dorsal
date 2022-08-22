from django.db import models
from django.contrib.auth import get_user_model
from wagtail.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Title(models.Model):
    title_name = models.CharField(max_length=30)
    def __str__(self):
        return self.title_name

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20,blank=True,null=True)
    title = models.ForeignKey(Title,on_delete=models.SET_NULL, blank=True,null=True)
    grade = models.IntegerField(blank=True,null=True)
    pronouns = models.CharField(max_length=15,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)