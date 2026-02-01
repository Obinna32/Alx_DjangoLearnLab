from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Viewset for editing and viewing books instances
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer