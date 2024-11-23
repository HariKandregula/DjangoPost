from django.urls import path
from . import views

urlpatterns = [
    path('post/<str:pk>', views.post, name='post'),
    path('home/', views.home, name='home'),
    path('home/createPost', views.createPost, name='createPost'),
    path('', views.signuppage, name='signuppage'),
    path('logout', views.logout_user, name='logout_user')
]
