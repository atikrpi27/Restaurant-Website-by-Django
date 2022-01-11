from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def reservation(request):
    return render(request,'reservation.html')

def team(request):
    return render(request,'team.html')

def special_dishes(request):
    return render(request,'special-dishes.html')