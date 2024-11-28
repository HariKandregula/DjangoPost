from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponseNotFound, HttpRequest
from django.template.context_processors import request

from .models import Customusers, Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.forms import userCreationForm
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def createPost(request):
    posts = Post.objects.all()
    if 'createPosts' in request.POST:
        user_created = Customusers()
        user_created.username = request.user
        user_created.save()
        posts = Post()
        posts.title = request.POST.get('postheading')
        posts.body = request.POST.get('postcontent')
        posts.userposted = user_created
        posts.save()
        # return render(request, 'home.html', {'posts': posts, 'user_name': user_name})
        return HttpResponseRedirect('/home')
        # return render(request, 'home.html', {'posts':posts})
    else:
        return render(request, 'createPost.html')


def post(request, pk):
    posts = Post.objects.get(id=pk)
    username = request.user
    if 'delete' in request.POST:
        posts.delete()
        return HttpResponseRedirect('/home')
    if 'likes' in request.POST:
        posts.likes += 1
        posts.save()
        # postsAll = Post.objects.all()
        return HttpResponseRedirect('/home')
        # return render(request, 'home.html', {'posts': postsAll})
    return render(request, 'post.html', {'posts': posts, 'username': username})  # 1st posts is template variable and 2nd posts in the view


def home(request):

    logger.debug('This is a debug log in home view')
    logger.warning("This is a warning log in home view")
    prof_pic = Customusers.objects.get(username=request.user).profile_pic
    posts = Post.objects.all()
    user_name = request.user
    all_users = None
    if 'new_user' in request.POST:
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        if User.objects.all().filter(username=username).exists():
            return HttpResponseNotFound()
        else:
            u = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                            password=password)
            custuser = Customusers()
            custuser.username = u
            # custuser.profile_pic = None
            custuser.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
        all_users = Customusers.objects.all().exclude(username=request.user)
        return render(request, 'home.html',
                      {'posts': posts,
                       'user_name': user_name,
                       'all_users': all_users})
    else:
        print("line 79 executed")
        if User.objects.all().filter(username=request.user).exists():
            all_users = Customusers.objects.all().exclude(username=request.user)
        else:
            return HttpResponseNotFound("Not logged in")
        return render(request, 'home.html', {'posts': posts, 'user_name': user_name, 'all_users': all_users, 'prof_pic': prof_pic})


def signuppage(request):
    if 'login_user' in request.POST:
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(request, username=username, password=password)
        if user.is_authenticated:
            login(request, user)
            request.session["has_logged"] = True
            return redirect('/home')
        else:
            return HttpResponseNotFound()
    if "has_logged" in request.session:
        if request.session["has_logged"]:
            print("This the session value," + str(request.session["has_logged"]))
            return HttpResponseRedirect('/home')
    context = {'form': userCreationForm()}
    return render(request, 'signuppage.html', context)


def logout_user(request):
    logout(request)
    # request.session.modified = True
    print("this is logout method")
    request.session["has_logged"] = False
    return HttpResponseRedirect('/')


def upload_profilepic(request):
    cust_user = Customusers.objects.get(username=request.user)
    print(cust_user)
    if request.method == 'POST':
        cust_user.profile_pic = request.FILES['profile-pic']
        print(cust_user.profile_pic)
        cust_user.save()
        return redirect('/home')
    return render(request, 'profile_pic.html')
