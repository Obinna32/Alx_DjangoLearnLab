from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

#BookListview handles GET requests to retrieve a list of all books
#Anyone can view the list

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #Define the backends for filtering, searching, and Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    #1. Filtering: Exact matches for these fields
    filterset_fields = ['title', 'author', 'publication_year']

    #2. Searching: Partial matches for these fields
    search_fields = ['title', 'author__name']

    #3. Ordering: Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title

#BoookDetailView handles Get requests to retrieve a book
#Accessible by everyone, but only authenticated users can see the details of the book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#BookCreateView handles Post requests to add a new book
#Restricted to Authenticated Users only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

#BookUpdateView handles PUT/PATCH requests to modify an existing book
#Restricted to Authenticated Users only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

#BookDeleteView handles Delete requests to remove a book
#Restricted to Authenticated Users only
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]