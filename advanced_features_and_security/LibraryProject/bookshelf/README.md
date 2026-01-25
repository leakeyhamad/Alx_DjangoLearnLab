Role-Based Access Control (RBAC) Documentation
Groups Defined:

Viewers: Can only access the list_books view.

Editors: Can view, create, and modify existing book entries.

Admins: Full CRUD (Create, Read, Update, Delete) capabilities.

Permission Enforcement: Permissions are enforced at the database level via Meta permissions and at the logic level using the @permission_required decorator in views.py. This ensures that even if a URL is manually typed, the user is blocked if they lack the required group membership.

Documentation
XSS Protection: Implemented via SECURE_BROWSER_XSS_FILTER and django-csp middleware to block malicious scripts.

CSRF Protection: Every state-changing form (POST) uses {% csrf_token %} to verify request authenticity.

SQL Injection: All database interactions are routed through Django’s ORM to ensure inputs are properly escaped/parameterized.

Session Security: Cookies are locked to HTTPS via SESSION_COOKIE_SECURE to prevent "Man-in-the-middle" attacks.

Testing Approach
Check Headers: Use a tool like curl -I or browser developer tools to verify X-Frame-Options: DENY is present.

CSRF Check: Try to submit a form without the {% csrf_token %} tag; it should return a 403 Forbidden error.

Input Check: Enter characters like ' or ; in the search bar. If the app displays results normally without crashing or executing code, your ORM usage is secure.