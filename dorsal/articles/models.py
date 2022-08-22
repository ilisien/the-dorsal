from django.db import models
from django.contrib.auth import get_user_model

from wagtail.fields import RichTextField
from wagtail.contrib.modeladmin.options import ModelAdmin


class Article(models.Model):

    class Section(models.TextChoices):
        UNASSIGNED = "UNA", "unassigned"
        AT_SCITECH = 'SCT', "at scitech"
        IN_PITTSBURGH = "PIT", "in pittsburgh"
        POLITICS = "POL", "politics"
        TECHNOLOGY = "TEC", "technology"
        SPORTS = "SPT", "sports"
        BLOG = "BLG", "blog"

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    # article stuff
    section = models.CharField(max_length=3, choices=Section.choices, default=Section.UNASSIGNED)
    title = models.CharField(max_length=100)
    pretext = models.TextField(blank=True)
    content = RichTextField(blank=True)

    # for author to change when done writing
    needs_approval = models.BooleanField(default=False)

    # for editors
    approved = models.BooleanField(default=False)
    approval_date = models.DateTimeField(blank=True,null=True)

    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
