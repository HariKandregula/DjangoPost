from django.db import models
from datetime import datetime

from django.utils.translation import gettext_lazy as _


# Create your models here.


class Customusers(models.Model):
    username = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(null=True, upload_to="pics")

    def __str__(self):
        return str(self.username)
 

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(blank=True, null=True, default=0)
    userposted = models.ForeignKey(to=Customusers, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)


class Comments(models.Model):
    comment_id = models.IntegerField(null=False)
    comments = models.CharField(max_length=1000)
    user_commented = models.ForeignKey(to=Customusers, on_delete=models.CASCADE)
