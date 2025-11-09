from django.contrib import admin
from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView, LibraryTemplateView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('list_books/', views.list_books, name='list_books'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('library/', views.LibraryDetailView.as_view(), name='library_books'),
    path('library-template', views.LibraryTemplateView.as_view(), name='library_page'),
    path('register/', views.register, name='registration'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name= 'logout'),
    path('Admin', views.admin_view, name='admin_view'),
    path('Librarian', views.librarian_view, name='librarian_view'),
    path('Member', views.member_view, name='member_view'),
    path('add_book/'),
    path('edit_book/'),
    path('delete_book/')
    ]