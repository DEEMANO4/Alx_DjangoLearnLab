from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView 
from django.views.generic import TemplateView, CreateView
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.urls import path

#

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    # context = {'books': books}
    return render(request,'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


#class LibraryDetailView(DetailView):
    #model = Library
    #template_name = 'relationship_app/library_detail.html'
    #context_object_name = 'library'  # This makes {{ library }} available in template
    
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    library = self.get_object()  # Gets the Library object
    #    # Add any extra context if needed
    #    context['total_books'] = library.books.count()
    #    return context

class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('registration_complete')
    template_name = 'register.html'


def is_admin(user):
    return user.is_superuser or user.groups.filter(name='admin').exists()

def is_librarian(user):
    return user.groups.filter(name='librarian').exists()

def is_member(user):
    return user.groups.filter(name='member').exists()



@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
@permission_required('relationship_app.can_manage_books')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request,'relationship_app/can_add_book.html' )
@permission_required('relationship_app.can_change_book')
def change_book(request):
    return render(request, 'relationship_add/can_change_book.html')
@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return render(request, 'relationship_app/can_delete_book')