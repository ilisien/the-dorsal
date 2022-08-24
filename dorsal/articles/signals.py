from django.db.models.signals import post_save
from django.dispatch import receiver
from articles.models import Article
from django.utils import timezone


@receiver(post_save, sender=Article)
def update_date_fields(sender,instance, **kwargs):
    # check all tick boxes, if any of them have changed, record the date
    if instance.needs_approval == True and instance.needs_approval_date == None:
        instance.needs_approval_date = timezone.now()
        instance.save()
    if instance.approved == True and instance.approved_date == None:
        instance.approved_date = timezone.now()
        instance.save()
    if instance.published == True and instance.pub_date == None:
        instance.pub_date = timezone.now()
        instance.save()

    # check all tick boxes for being unchecked, if they are, remove the date
    if instance.needs_approval == False and instance.needs_approval_date != None:
        instance.needs_approval_date = None
        instance.save()
    if instance.approved == False and instance.approved_date != None:
        instance.approved_date = None 
        instance.save()
    if instance.published == False and instance.pub_date != None:
        instance.pub_date = None
        instance.save()
    