from pydoc import pager
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import RegForm
from user.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('con_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if password == c_password:
            # for create user in User table from reg html form
            user = User.objects.create_user(username=username, password=password)
            user.set_password(password)
            user.save()

            # for save Ragistration table
            reg = Registration(first_name=fname, last_name = lname, username=username, email = email, phone = phone, password= password, con_password = password)
            reg.save()
            return redirect('login')
        else:
            messages.info(request,'Password and Confirm Password does not match.')
    return render(request,'reg.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Invalid username or password')

    return render(request,'login.html')

def userLogout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request,'profile.html')
