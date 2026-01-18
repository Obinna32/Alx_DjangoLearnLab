from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

# Create your views here.

from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# Class-based view: show one library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
