from relationship_app.models import Author, Book, Library, Librarian 

all_books = Library.objects.get(name='Library_name')
books =Library.books.all()