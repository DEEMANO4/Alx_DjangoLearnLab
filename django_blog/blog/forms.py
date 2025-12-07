from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django import forms

class PostRegistrationForm(UserCreationForm):
    class Meta:
        model = Post
        fields = ('email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']