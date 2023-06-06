from django.shortcuts import render
from .models import Post
from .forms import userCreationForm

# Create your views here.

def createPost(request):
    #ts = Post.objects.all()
    #return render(request, 'createID.html', {'posts': posts})
    return render(request, 'createPost.html')

def signuppage(request):
    return render(request, 'signuppage.html')

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})

def home(request):
    '''
    posts = Post.objects.all()
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('postheading')
        post.body = request.POST.get('postcontent')
        return render(request, 'home.html', {'posts': posts})
        post.save()'''
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def createUser(request):
    if request.method =='POST':
        #user = Users()
        '''
        username1 = request.POST['username']
        password1 = request.POST['password']
        new_user = Users.objects.create(username = username1, password = password1)
        new_user.save()
    return render(request, 'home.html')'''
        form = userCreationForm(request.POST)
        