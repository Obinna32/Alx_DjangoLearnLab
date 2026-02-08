# Advanced API Project - Book Management

## Endpoints
- `GET /api/books/`: List all books (Public).
- `GET /api/books/<id>/`: View specific book details (Public).
- `POST /api/books/create/`: Add a new book (Authenticated Users).
- `PUT /api/books/update/`: Edit a book (Authenticated Users).
- `DELETE /api/books/delete/`: Remove a book (Authenticated Users).

## Permissions
- **Read Access:** Unauthenticated users can view the list and details of books.
- **Write Access:** Creating, Updating, and Deleting requires a valid user token/session.

## Validation
- Books cannot be saved with a `publication_year` that is in the future.

## Advanced Query Features

The `Book List` endpoint (`/api/books/`) supports the following features:

### 1. Filtering
Filter results by exact matches using query parameters:
- `title`: `/api/books/?title=1984`
- `author`: `/api/books/?author=1`
- `publication_year`: `/api/books/?publication_year=1950`

### 2. Searching
Perform a text search across `title` and `author name` using the `search` parameter:
- Example: `/api/books/?search=George+Orwell`

### 3. Ordering
Sort the results using the `ordering` parameter:
- `title` (A-Z): `/api/books/?ordering=title`
- `title` (Z-A): `/api/books/?ordering=-title`
- `publication_year`: `/api/books/?ordering=publication_year`