from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # FBV URL
    path('books/', list_books, name='list_books'),
    
    # CBV URL - 'pk' stands for Primary Key, which Django uses to find the library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]