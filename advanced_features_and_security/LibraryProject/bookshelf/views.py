from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import permission_required
# Create your views here.
# @permission_required('bookshelf.can_create', raise_exception=True)
# @permission_required('bookshelf.can_edit', raise_exception=True)
# @permission_required('bookshelf.can_delete', raise_exception=True)

# books/views.py
# from django.shortcuts import render
# from django.contrib.auth.decorators import permission_required
# from .models import Book
# from .forms import BookForm

@permission_required('books.can_create_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@permission_required('books.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

@permission_required('books.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

# This view might not require specific book-level permissions,
# but rather general "view" permission if you want to restrict it.
# @permission_required('books.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})