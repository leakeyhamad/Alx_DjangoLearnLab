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

Deployment Configuration (Nginx Example)
In a real production environment, Django (via Gunicorn) doesn't handle the SSL handshake itself. A reverse proxy like Nginx or Apache handles the certificates.

Example Nginx Configuration Snippet:

Nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri; # Force redirect to HTTPS
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme; # Crucial for Django's SECURE_SSL_REDIRECT
    }
}

Security Review ReportFeatureProtection ProvidedHSTSPrevents "SSL Stripping" attacks by forcing the browser to remember to use HTTPS before even attempting a request.Secure CookiesPrevents cookies from being leaked over unencrypted Wi-Fi or "man-in-the-middle" interceptions.X-Frame-OptionsStops malicious sites from overlaying your UI inside an invisible frame to steal clicks (Clickjacking).MIME SniffingForces the browser to strictly follow the Content-Type header, preventing attackers from disguising scripts as images.