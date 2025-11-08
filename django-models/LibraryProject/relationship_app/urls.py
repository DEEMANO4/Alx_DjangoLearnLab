from django.contrib import admin
from django.urls import path
from relationship_app import views
from .views import list_books, LibraryDetailView
urlpatterns = [
   # path('', views.index, name='index'),
    #path('about/', views.about, name='about')
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list_books'),
    path('library/', views.LibraryDetailView.as_view(), name='library_books')

]