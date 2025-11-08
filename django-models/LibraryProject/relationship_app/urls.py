from django.contrib import admin
from django.urls import path
from relationship_app import views

urlpatterns = [
   # path('', views.index, name='index'),
    #path('about/', views.about, name='about')
    path('admin/', admin.site.urls)
    path('books/', views.book_list, name='list_books')
]