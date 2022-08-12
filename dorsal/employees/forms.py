from django import forms
from employees.models import Employee

class CustomProfileForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ['user']