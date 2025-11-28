# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from .models import Book
# from .serializers import BookSerializer


# class BookAPITestCase(APITestCase):
#     def setup(self):
#         self.book1 = Book.objects.create(title="Test Book 1", author="Author A", publication_year =2020)
#         self.book2 = Book.objects.create(title="Title Book 2", author="Author B", publication_year=2021)
#         self.list_url = reverse('book_list')


#     def test_get_book_list(self):
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         expected_data = BookSerializer([self.book1, self.book2], many=True)
#         self.assertEqual(response.data, expected_data)



#     def test_get_book_detail(self):
#         detail_url = reverse('book_detail', kwargs={'pk': self.book1.pk}) 
#         response = self.client.get(detail_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         expected_data = BookSerializer(self.book1).data
#         self.assertEqual(response.data, expected_data)


#     def test_create_book(self):
#         new_book_data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
#         response = self.client.post(self.list_url, new_book_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(Book.objects.filter(title='New Book').exists())


#     def test_update_book(self):
#         detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
#         updated_data = {'title': 'Updated Title', 'author': 'Author A', 'publication_year': 2020}
#         response = self.client.put(detail_url, updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.book1.refresh_from_db()
#         self.assertEqual(self.book1.title, 'Updated Title')


    # def test_delete_book(self):
    #     detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
    #     response = self.client.delete(detail_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())  





from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Book # Assuming your Book model is in the same app
from .serializers import BookSerializer # Assuming your BookSerializer is in the same app

User = get_user_model()

class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book_data = {'title': 'Test Book', 'author': 'Test Author', 'isbn': '1234567890'}
        self.book = Book.objects.create(**self.book_data)
        self.list_url = reverse('book-list') # Assuming 'book-list' is the name of your list endpoint
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk}) # Assuming 'book-detail' is the name of your detail endpoint

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.list_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2) # Initial book + new book

    def test_create_book_unauthenticated(self):
        response = self.client.post(self.list_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        updated_data = {'title': 'Updated Book', 'author': 'Updated Author', 'isbn': '0987654321'}
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
