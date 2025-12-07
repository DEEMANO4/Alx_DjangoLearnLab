from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import PostForm
from .forms import PostRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = PostRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PostRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.author = request.user
            post_instance.save()
            messages.success(request, f'Your post has been created')
            return redirect(post_instance.get_absolute_url())
    else:
        form = PostForm()

    context = {
        'form': form,
        'title': 'New Post'
    }
    return render(request, 'blog/post_form.html', context)


def manage_comment(request, comment_id=None):
    comment = get_object_or_404(Comment, pk=comment_id) if comment_id else None
    form = CommentForm(request.POST or None, instance=comment)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect('success_url_name')
    return render(request, 'comments/comment_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status='published')
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.Method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm

        return render(request, 'blog/post_detail.html', {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        })
    
class CommentUpdateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)

        form.instance.post = post
        form.instance.name = self.request.user.username
        form.instance.email = self.request.user.email

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})


    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username or self.request.user.is_superuser
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username or self.request.user.is_superuser
