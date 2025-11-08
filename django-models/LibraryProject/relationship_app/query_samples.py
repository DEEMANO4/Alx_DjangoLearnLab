from relationship_app.models import Author, Book, Library, Librarian 

"Library.objects.get(name=library_name)"
books =Library.books.all()

author = Author.objects.get(name='author_name')
Author.objects.filter(author=author)
