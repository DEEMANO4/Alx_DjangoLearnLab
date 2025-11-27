from rest_framework import serializers
from .models import Book, Author
import datetime 

class BookSerializer(serializers.ModelSerializer):
    # Creating the book serializer with its fields from the Book model
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

     # raising an error when date exceeds today's date
        def validate_publication_year(self, value):
            current_year = datetime.date.today().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

class AuthorSerializer(serializers.ModelSerializer):
    # Creating the author serializer with the 'name' field from the Author model and related books
    books =BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']