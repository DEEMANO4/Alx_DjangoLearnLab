from django.db import models
from datetime import datetime
# Create your models here.
class Author(models.Model):
    # Creating the Author model
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Creating the Book model 
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return f"Title {self.title} by {self.author}."