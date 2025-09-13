from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Create groups
        editors_group, _ = Group.objects.get_or_create(name="Editors")
        viewers_group, _ = Group.objects.get_or_create(name="Viewers")
        admins_group, _ = Group.objects.get_or_create(name="Admins")

        # Fetch permissions by codename
        can_view = Permission.objects.get(codename="can_view_book")
        can_create = Permission.objects.get(codename="can_create_book")
        can_edit = Permission.objects.get(codename="can_edit_book")
        can_delete = Permission.objects.get(codename="can_delete_book")

        # Assign permissions to groups
        editors_group.permissions.set([can_view, can_create, can_edit])
        viewers_group.permissions.set([can_view])
        admins_group.permissions.set([can_view, can_create, can_edit, can_delete])

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully."))

