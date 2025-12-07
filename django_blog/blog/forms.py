from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Post, Comment
from django import forms
from django.core.exceptions import ValidationError

# User = get_user_model()

class PostRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Must be a valid email address.')
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        return name.capitalize()
        
    def clean(self):
        cleaned_data = super().clean()
        body = cleaned_data.get("body")
        if body and "spam" in body.lower():
            raise ValidationError("Comments containing 'spam' are not allowed.")
        return cleaned_data