from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from savvyapp.forms import Userinfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .forms import LoginForm

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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, "index.html", {'form': form})

def signup(request):
    if request.method == "POST":
        form = Userinfo(request.POST)
        if form.is_valid():
            try:
                form.save() 
                messages.success(request, 'Signup successful, please login')
                return redirect('homePage')
            except Exception as e:
                messages.error(request, f'An error occurred. Please try again: {e}')
    else:
        form = Userinfo()
    return render(request, "index.html", {'form': form})


def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    post_list = [{"content": post.content, "created_at": post.created_at} for post in posts]
    return JsonResponse(post_list, safe=False)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        if title and content: 
            post = Post.objects.create(title=title, content=content)
            return JsonResponse({'id': post.id, 'title': post.title, 'content': post.content})
        return JsonResponse({'error': 'Title and content are required'}, status=400)

@csrf_exempt
def list_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    data = [{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]
    return JsonResponse(data, safe=False)

