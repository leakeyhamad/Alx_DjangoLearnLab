Role-Based Access Control (RBAC) Documentation
Groups Defined:

Viewers: Can only access the list_books view.

Editors: Can view, create, and modify existing book entries.

Admins: Full CRUD (Create, Read, Update, Delete) capabilities.

Permission Enforcement: Permissions are enforced at the database level via Meta permissions and at the logic level using the @permission_required decorator in views.py. This ensures that even if a URL is manually typed, the user is blocked if they lack the required group membership.