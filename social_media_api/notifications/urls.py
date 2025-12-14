from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/like/', views.like_post, name='like-post'),
    path('post/<int:pk>/unlike/', views.unlike_post, name='unlike-post'),
]