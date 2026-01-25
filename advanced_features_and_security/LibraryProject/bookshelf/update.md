**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)