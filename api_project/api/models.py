from django.db import models
# from django.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)