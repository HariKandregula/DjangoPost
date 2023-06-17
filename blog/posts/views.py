from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from blog.forms import userCreationForm

# Create your views here.

def createPost(request):
    posts = Post.objects.all()
    #return render(request, 'createID.html', {'posts': posts})
    return render(request, 'createPost.html')

def post(request, pk):
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
        posts.delete()
        return HttpResponseRedirect('/home')
    return render(request, 'post.html', {'posts': posts})

def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('postheading')
        post.body = request.POST.get('postcontent')
        post.save()
    return render(request, 'home.html', {'posts': posts})
