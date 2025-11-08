from relationship_app.models import Author, Book, Library, Librarian 

author = Author.objects.get(id=1)

if author:
    books_by_author = Book.objects.filter(author=author)