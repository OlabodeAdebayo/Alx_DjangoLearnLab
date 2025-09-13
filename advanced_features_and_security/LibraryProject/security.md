# Security Measures Implemented

1. DEBUG set to False in production.
2. Browser-side protections: XSS filter, X-Frame-Options, Content-Type Nosniff.
3. CSRF tokens used in all forms.
4. Secure cookies (CSRF & session) over HTTPS only.
5. All database queries use ORM to prevent SQL injection.
6. Input validation handled via Django forms.
7. Optional CSP headers added to reduce XSS risks.
