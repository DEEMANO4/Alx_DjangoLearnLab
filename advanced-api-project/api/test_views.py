from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from .serializers import BookSerializer


class BookAPITestCase(APITestCase):
    def setup(self):
        self.book1 = Book.objects.create(title="Test Book 1", author="Author A", publication_year =2020)
        self.book2 = Book.objects.create(title="Title Book 2", author="Author B", publication_year=2021)







