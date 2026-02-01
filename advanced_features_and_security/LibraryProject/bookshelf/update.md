In [4]: book = Book.objects.get(id=1)

In [5]: book.title = "Nineteen Eighty-Four"

In [6]: book.save()