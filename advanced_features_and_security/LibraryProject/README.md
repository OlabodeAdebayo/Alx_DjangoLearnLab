# Groups & Permissions Setup

- **Viewers** → can_view_book
- **Editors** → can_view_book, can_create_book, can_edit_book
- **Admins** → can_view_book, can_create_book, can_edit_book, can_delete_book

## Testing
1. Run `python manage.py create_groups` to set up groups/permissions.
2. Create users and assign them to groups.
3. Log in and verify restricted views:
   - Viewers: Only see books
   - Editors: Create/Edit books
   - Admins: Full control

