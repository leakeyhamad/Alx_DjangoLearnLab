from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add new fields to the user list view
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    
    # fieldsets controls the "Edit User" page
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # add_fieldsets controls the "Add User" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

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