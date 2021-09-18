from django.http import request
from django.shortcuts import render,redirect

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from .forms import RegisterUser

# Create your views here.
def homeview(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)

def userregister(request):
    form=RegisterUser()
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def Loginview(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        user=authenticate(username=u,password=p)

        if user is not None:
            print('valid credentials')
            print('Actual Login code')
            login(request,user)
            return redirect('home')

        else:
            print('Invalid credentials')
            messages.error(request,'Invalid cradentials')

    template_name='login.html'
    context={}
    return render(request,template_name,context)

def logoutview(request):
    logout(request)
    return redirect('login')

# def changepasswordview(request):
#     if request.method=='POST':
#         u=request.POST.get('un')
#         p=request.POST.get('pw')
#         new=request.POST.get('unew')
#         con=request.POST.get('pnew')
#         user=authenticate(username=u,password=p)
#         if user and new==con:
#             usr=user.objects.get(username=u)
#             co=str(con)
#             usr.user_password(co)
#             usr.save()
#             return redirect('login')
#         else:
#             messages.error(request,'please enter valid credentials')
#     template_name='change.html'
#     context={}
#     return render(request,template_name,context)

def changepasswordview(request):
    form = PasswordChangeForm(request.user)
    if request.method=='POST':
        form =PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)#one type of session
            messages.success(request,'your password was successfully changed')
            return redirect('login')
        else:
            messages.error((request,'please cheack your password once'))
    template_name='change.html'
    context={'form':form}
    return render(request,template_name,context)

