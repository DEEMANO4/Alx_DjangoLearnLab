from django.contrib import admin
from django.urls import path
from relationship_app import views
from .views import list_books, LibraryDetailView, LibraryTemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_books'),
    path('library-template', views.LibraryTemplateView.as_view(), name='library_page'),
    ]