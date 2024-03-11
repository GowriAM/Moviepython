from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from actor.form import UserForm


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return  redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        Confirmpassword1=request.POST['password1']
        if password==Confirmpassword1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return  redirect('register')
            elif User.objects.filter(first_name=first_name).exists():
                messages.info(request,"Try Again...")
                return  redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                messages.info(request, "successful registration")
                return  redirect('login')

            # print("user created")
        else:
            messages.info(request,"password not matching")

            return  redirect('register')
        return  redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def update(request,id):
    user=User.objects.get(id=id)
    form=UserForm(request.POST or None, request.FILES,instance=user)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'edit.html',{'form':form,'user':user})