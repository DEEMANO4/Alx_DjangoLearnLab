from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.views.generic import TemplateView, CreateView
from relationship_app.models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
]

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request,'relationship_app/list_books.html', context)

class LibraryTemplateView(TemplateView):
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_data'] = 'Another example'



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_rating'] = book.get_average_rating()

class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('register')
    template_name = '.html'