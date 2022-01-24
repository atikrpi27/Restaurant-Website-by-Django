from django import forms
from django.forms import fields
from user.models import Registration

class RegForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields= "__all__"