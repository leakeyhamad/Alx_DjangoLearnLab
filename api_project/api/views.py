from django.shortcuts import render
from rest_framework import viewsets, permissions

# Create your views here.
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]