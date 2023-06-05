from django.urls import path
from . import views

urlpatterns = [
    path('post/<str:pk>', views.post, name='post'),
    path('', views.home, name='home'),
    path('home/createPost', views.createPost, name='createPost'),
    path('home/signuppage', views.signuppage, name='signuppage')
]
