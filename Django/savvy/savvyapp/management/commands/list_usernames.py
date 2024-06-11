from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'List all existing usernames in the database'

    def handle(self, *args, **options):
        usernames = User.objects.values_list('username', flat=True)
        self.stdout.write('\n'.join(usernames))
