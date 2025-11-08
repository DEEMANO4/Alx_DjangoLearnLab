from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request,'books/book_list.html', context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['avereage_rating'] = book.get_average_rating()