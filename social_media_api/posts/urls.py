from django.urls import path
from .views import PostViewSet, CommentViewSet

post_list = PostViewSet.as_view({'get': 'list', 'post': 'create'})
post_detail = PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

comment_list = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
comment_detail = CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})


urlpatterns = [
    path('post/', post_list, name='post-list'),
    path('posts/<intLpk>/', post_detail, name='post-detail'),
    path('posts/<int:post_pk>/comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>/', comment_detail, name='comment-detail')
    path('feed/', UserFeedView.as_view(), name='user-feed')
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    # path('posts/<ink:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    # path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

]