from pydoc import pager
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import RegForm
from user.models import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def registration(request):
    if request.method == 'POST':
        # form = RegForm(request.POST or None)
        # if form.is_valid():
            # form.save()
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('con_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        user = User.objects.create_user(username=username, password=password)
        user.set_password(password)
        user.save()
        reg = Registration(first_name=fname, last_name = lname, username=username, email = email, phone = phone, password= password, con_password = password)
        reg.save()
        return redirect('login')
    return render(request,'reg.html')

def userlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('Invalid username or password')

    return render(request,'login.html')
