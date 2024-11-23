from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponseNotFound
from posts.models import Customusers, Post
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
    return render(request, 'post.html',
                  {'posts': posts, 'username': username})  # 1st posts is template variable and 2nd posts in the view


def home(request):
    logger.debug('This is a debug log in home view')
    logger.warning("This is a warning log in home view")
    posts = Post.objects.all()
    user_name = request.user
    print("Current user is: ", user_name)
    if 'new_user' in request.POST:
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        if User.objects.all().filter(username=username).exists():
            return HttpResponseNotFound()
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                            password=password)
        return render(request, 'home.html', {'posts': posts, 'user_name': user_name})

    else:
        print("line 62 executed")
        return render(request, 'home.html', {'posts': posts, 'user_name': user_name})


def signuppage(request):
    if 'login_user' in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # if user is not None:
        if user.is_authenticated:
            login(request, user)
            request.session["has_logged"] = True
            return HttpResponseRedirect('/home')
            # return home(request)
            # return render(request, 'home.html', {'posts': posts, 'user_name': user_name})
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
