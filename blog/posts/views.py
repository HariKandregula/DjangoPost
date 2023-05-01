from django.shortcuts import render
from .models import Post


# Create your views here.

def createID(request):
    posts = Post.objects.all()
    return render(request, 'createID.html', {'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

