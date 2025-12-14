from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like
from notifications.models import Notification


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        if 'post_pk' in self.kwargs:
            return Comment.objects.filter(post_pk=self.kwargs['post_pk'])
        return Comment.objects.all()

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)


class UserFeedView(generics.ListAPIView):
    serializer_class =PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()

        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')

        return queryset

rom django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like, Notification
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response



class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        post =generics.get_object_or_404(Post, pk=pk)
        Like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb= 'liked',
                    target=post
                )
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        return Response({"detail":"You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like_filter = Like.objects.filter(user=request.user, post=post).delete()

        if like_filter.exists():
            content_type = ContentType.objects.get_for_model(post)
            Notification.objects.filter(
                actor=request.user,
                verb='liked',
                target_content_type=content_type,
                target_object_id=post.id
            ).delete()

            like_filter.delete()
            return Response({"detail": "Post unlike successfully."}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    


# generics.get_object_or_404(Post, pk=pk)










# class PostListCreateView(generics.ListCreateApiView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

#     class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#         queryset = Post.objects.all()
#         serializer_class = PostSerializer
#         permission_classes =[permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]


# class CommentListCreateView(generics.ListCreateApiView):
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

#     def get_qyeryset(self):
#         post_pk =self.kwargs['post_pk']
#         return Comment.objects.filter(post_pk=post_pk)

#     def perform_create(self, serializer):
#         post = Post.objects.get(pk=self.kwargs['post_pk'])
#         serializer.save(author=self.equest.user, post=post)

# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
#     lookup_field = 'pk'