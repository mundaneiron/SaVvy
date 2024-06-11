from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from savvyapp.forms import Userinfo

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
            )
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully signed in.')
            return redirect('homePage')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, "index.html")
        

def insert(request):
    if request.method == "POST":
        form = Userinfo(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Signup successful, please login.')
                return redirect('homePage')
            except:
                messages.error(request, 'An error occurred. Please try again.')
    else:
        form = Userinfo()
    return render(request, "index.html", {'form':form})
