from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_create
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # Logic for editing goes here...
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book goes here...
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic for deleting a book goes here...
    pass
