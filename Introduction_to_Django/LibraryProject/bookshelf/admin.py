from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Customizing the Admin interface
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a filter sidebar for the publication year
    list_filter = ('publication_year',)
    
    # Enable search for title and author
    search_fields = ('title', 'author')

# Register the model with the custom configuration
admin.site.register(Book, BookAdmin)