from django.urls import path
from .views import BookList

path('books/', BookList.as_view(), name='boo-list')