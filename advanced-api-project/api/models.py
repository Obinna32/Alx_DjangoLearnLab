from django.db import models

# Create your models here.

# The Author model represents a person who writes books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# The Book model represents a book written by an author.
# It has a Foreign Key to Author, creating a one-to-many relationship.

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # The related_name 'books' allows us to access all books of an author using author.books.all()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title