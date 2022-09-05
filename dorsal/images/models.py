from django.db import models
from staff.models import Profile
from wagtail.images.models import Image, AbstractImage, AbstractRendition


class InfoImage(AbstractImage):
    photographer = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True,blank=True)
    caption = models.CharField(max_length=255, blank=True)
    date_taken = models.DateTimeField(blank=True,null=True)

    admin_form_fields = Image.admin_form_fields + (
        'photographer',
        'caption',
        'date_taken',
    )



class InfoImageRendition(AbstractRendition):
    image = models.ForeignKey(InfoImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ("image","filter_spec","focal_point_key"),
        )