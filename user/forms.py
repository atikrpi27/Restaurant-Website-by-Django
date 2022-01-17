from django import forms
from django.forms import fields
from . models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields= "__all__"