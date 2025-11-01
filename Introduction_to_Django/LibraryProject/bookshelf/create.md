from myapp.models import Book
books = Book.objects.create(title="1984", author="George Orwel", publication_year="1949")