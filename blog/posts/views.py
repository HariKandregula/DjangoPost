from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponseNotFound
from .models import Post, Customusers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def createPost(request):
    posts = Post.objects.all()
    user_name = request.user
    if 'createPosts' in request.POST:
        posts = Post()
        posts.title = request.POST.get('postheading')
        posts.body = request.POST.get('postcontent')
        Customusers(username=user_name).posted.add(posts.id)
        # user_name.customusers.add(posts)
        posts.save()
        # return render(request, 'home.html', {'posts': posts, 'user_name': user_name})
        return HttpResponseRedirect('/home')
    else:
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
    print("Current user is: ",user_name)
    if 'logout' in request.POST:
        print("logout successfull")
        return logout(request)
    if 'new_user' in request.POST:
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        if User.objects.all().filter(username=username).exists():
            return HttpResponseNotFound()
        else:
            user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
        return render(request, 'home.html', {'posts': posts, 'user_name': user_name})
    if 'login_user' in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseNotFound()
    else:
        return render(request, 'home.html', {'posts': posts, 'user_name': user_name})

def signuppage(request):
    return render(request, 'signuppage.html')
    