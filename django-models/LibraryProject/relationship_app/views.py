from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.views.generic import TemplateView, CreateView
from relationship_app.models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
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