from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like, Notification
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


# Create y our views here 
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

