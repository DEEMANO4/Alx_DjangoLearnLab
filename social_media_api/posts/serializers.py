from rest_framework import serializers
from .models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields =['id', 'author', 'content', 'created_at', 'post']

        read_only_fields = ['author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'comments']
        read_only_fields = ['author', 'created_at']
        extra_kwargs = {
            'title': {'max_length': 100},
        }

    def validate_title(self, value):
        if len(value.split()) < 3:
            raise serializers.ValidationError('Title must be at least 3 words long.')
        return value