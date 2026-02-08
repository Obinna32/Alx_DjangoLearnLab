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