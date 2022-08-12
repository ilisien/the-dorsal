from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Article(models.Model):
    title = models.TextField(max_length=100)