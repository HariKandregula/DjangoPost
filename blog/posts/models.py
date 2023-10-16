from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    likes = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title


class Customusers(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username