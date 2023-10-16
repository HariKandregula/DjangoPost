from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Post, Customusers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 

# Create your views here.

def createPost(request):
    posts = Post.objects.all()
    #return render(request, 'createID.html', {'posts': posts})
    return render(request, 'createPost.html')

def post(request, pk):
    posts = Post.objects.get(id=pk)
    if 'delete' in request.POST:
        posts.delete()
        return HttpResponseRedirect('/home')
    if 'likes' in request.POST:
        posts.likes += 1
        posts.save()
        postsAll = Post.objects.all()
        return HttpResponseRedirect('/home')
        #return render(request, 'home.html', {'posts': postsAll})
    return render(request, 'post.html', {'posts': posts})#1st posts is template variable and 2nd posts in the view

def home(request):
    posts = Post.objects.all()
    user_name = request.user
    if request.method == 'POST' and 'newPost' in request.POST:
        post = Post()
        post.title = request.POST.get('postheading')
        post.body = request.POST.get('postcontent')
        post.save()
        return render(request, 'home.html', {'posts': posts, 'user_name': user_name})
    return render(request, 'home.html', {'posts': posts, 'user_name': user_name})

def signuppage(request):
    posts = Post.objects.all()
    user_name = request.user
    if 'new_user' in request.POST:
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        if User.objects.all().filter(username=username).exists():
            return HttpResponseNotFound()
        else:
            user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
        return home(request)
    elif 'login_user' in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponseNotFound()
        return home(request)
    else:
        return render(request, 'signuppage.html')