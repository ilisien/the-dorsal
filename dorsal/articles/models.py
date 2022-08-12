from django.db import models

from wagtail.fields import RichTextField


class Article(models.Model):
    title = models.TextField(max_length=100)