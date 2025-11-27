from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('books', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='create_book'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='update_book'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book')
]