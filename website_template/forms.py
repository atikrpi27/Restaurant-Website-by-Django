from django import forms
from django.forms import fields
from . models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        # fields = ['Food_name','Food_Catagories','food_price']
        fields= "__all__"