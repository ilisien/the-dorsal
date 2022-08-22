from django import forms

from django.contrib.auth import get_user_model
from staff.models import Profile

from wagtail.users.forms import UserEditForm, UserCreationForm

class ProfileSettingsForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']