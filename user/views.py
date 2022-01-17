from django.shortcuts import render
from django.http import HttpResponse
from user.forms import RegForm

from user.models import Reg

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'reg.html')
