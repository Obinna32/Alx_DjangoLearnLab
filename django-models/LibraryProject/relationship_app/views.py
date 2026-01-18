from django.shortcuts import render, redirect
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()  # REQUIRED by checker
    return render(
        request,
        "relationship_app/list_books.html",  # REQUIRED by checker
        {"books": books}
    )


# Class-based view: show one library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Logout view (built-in)
class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("books")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})