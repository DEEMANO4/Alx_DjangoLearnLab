from relationship_app.models import Author, Book, Library, Librarian 

all_books = Library.objects.get(name='library_name')
books =Library.books.all()