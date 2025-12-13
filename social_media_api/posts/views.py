from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, permissions

# Create your views here.

class PostViewSet(Viewsets.ModelViewSet):
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
        post Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)







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