from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from staff.models import Profile

@receiver(post_save, sender=get_user_model())
def create_related_profile(sender, instance, created, **kwargs):
    # when a new User instance is saved:
    # - check if the instance is new
    # - create a Profile for the user
    if not created:
        return
    instance.profile = Profile.objects.create(user=instance)