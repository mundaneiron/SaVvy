from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

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
            username = user.username
            return render(request, "index.html", {'username': username})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('homePage')

    if request.method == "POST":
        newEmail = request.POST.get('newEmail')
        newUserName = request.POST.get('newUserName')
        newPassword = request.POST.get('newPassword')
        reenterPassword = request.POST.get('reenterPassword')

        newUser = User.objects.create_user(
            username=newUserName,
            email=newEmail,
            password=newPassword
        )
        newUser.save()
        messages.success(request, "Your Account has been successfully created.")
        return redirect('homePage')
    
    return render(request, "index.html")

