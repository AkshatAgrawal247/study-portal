from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .form import *
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user,allowed_users
from teacher.models import Tutor
from student.models import Stud

def logoutuser(request):
    logout(request)
    return redirect('/home/login')

@unauthenticated_user
def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/thome/')
        else:
            messages.info(request,'Username or Password is incorrect')

    return render(request, 'login.html')

@unauthenticated_user
def home(request):
    return render(request, 'home.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            role = form.cleaned_data.get('group')
            if role=='teacher':
                Tutor.objects.create(user=user,)
            if role=='student':
                Stud.objects.create(user=user,)
            group =Group.objects.get(name=role)
            print(group,role)
            user.groups.add(group)

            username=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+username)
            return redirect('/home/login')

    context = {'form':form}
    return render(request, 'register.html',context)


