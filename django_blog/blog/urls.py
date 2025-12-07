from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name=('blog-home')),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'), 
    path('search/', views.search_results, name='search_results'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag')  
]