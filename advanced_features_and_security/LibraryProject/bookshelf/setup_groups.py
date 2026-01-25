from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

def setup_groups():
    # Get the content type for the Book model
    content_type = ContentType.objects.get_for_model(Book)
    
    # Create Groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    
    # Assign Permissions
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    editors.permissions.add(can_edit)