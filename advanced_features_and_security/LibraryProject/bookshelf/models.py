from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True,blank=True)
    profile_photo = models.ImageField(upload_to='images', null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        permissions = (
            ('can_view', 'can_create', 'can_edit', 'can_delete'
            '')
        )


class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo):
        user = self.model(date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, date_of_birth, profile_photo):
        return super().creat_superuser(date_of_birth,profile_photo)

    def __str__(self):
        return self.username