from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings 
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField( settings.AUTH_USER_MODEL, symmetrical=False, related_name='followed_by', blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name='followings', blank=True)

    def __str__(self):
        return self.username
    
    def count_followers(self):
        return self.followed_by.count()
