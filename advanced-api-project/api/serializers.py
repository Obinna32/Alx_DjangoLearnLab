from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
     """
    Serializer for the Book model.
    Includes custom validation for the publication year.
    """
     class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

        # Custom validation: ensure publication_year is not in the future
        def validate_publication_year(self, value):
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested BookSerializer to show all books associated with an author.
    """
    # The 'books' field here matches the 'related_name' in our Book model.
    # We set many=True because one author can have many books.
    # read_only=True ensures books are handled automatically based on relationships.

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

        