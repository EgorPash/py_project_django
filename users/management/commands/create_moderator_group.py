from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product

class Command(BaseCommand):
    help = 'Create Moderator Group'

    def handle(self, *args, **options):
        moderators_group, created = Group.objects.get_or_create(name='Moderators')

        permissions = [
            'catalog.can_unpublish_product',
            'catalog.can_change_description',
            'catalog.can_change_category',
        ]

        for perm in permissions:
            permission = Permission.objects.get(codename=perm.split('.')[-1])
            moderators_group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Successfully created Moderator group with permissions'))