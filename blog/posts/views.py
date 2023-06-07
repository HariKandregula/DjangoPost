from django.shortcuts import render
from .models import Post
from blog.forms import userCreationForm

# Create your views here.

def createPost(request):
    posts = Post.objects.all()
    #return render(request, 'createID.html', {'posts': posts})
    return render(request, 'createPost.html')

def signuppage(request):
    return render(request, 'signuppage.html')

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})

def home(request):
    posts = Post.objects.all()
    if request.method == 'POST' and request.POST.get('name') == 'new_post':
        post = Post()
        post.title = request.POST.get('postheading')
        post.body = request.POST.get('postcontent')
        post.save()
    
    if request.method =='POST' and request.POST.get('name') == 'new_user':
        user = Users.objects.all()
        '''
        username1 = request.POST['username']
        password1 = request.POST['password']
        new_user = Users.objects.create(username = username1, password = password1)'''
        new_user = Users()
        new_user.username  = request.POST['username']
        new_user.password = request.POST['password']
        new_user.save()
    return render(request, 'home.html', {'posts': posts})

def createUser(request):
    if request.method =='POST1':
        user = Users().objects.all()
        username1 = request.POST['username']
        password1 = request.POST['password']
        new_user = Users.objects.create(username = username1, password = password1)
        new_user.save()
    return render(request, 'home.html')
        