from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from savvyapp.forms import Userinfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .forms import LoginForm
from .models import Userdetails

import json

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = Userdetails.objects.get(username=username, password=password)
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful')
                return redirect('home')
            except Userdetails.DoesNotExist:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, "index.html", {'form': form})

def insert(request):
    if request.method == "POST":
        form = Userinfo(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Signup successful, please login')
                return redirect('homePage')
            except:
                messages.error(request, 'An error occurred. Please try again')
    else:
        form = Userinfo()
    return render(request, "index.html", {'form':form})


def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    post_list = [{"content": post.content, "created_at": post.created_at} for post in posts]
    return JsonResponse(post_list, safe=False)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(content=data['content'])
        return JsonResponse({"id": post.id, "content": post.content, "created_at": post.created_at})

