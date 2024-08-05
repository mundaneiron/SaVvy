from django.core.management.base import BaseCommand
from savvyapp.models import Userdetails

class Command(BaseCommand):
    help = 'Hash plain text passwords for existing users'

    def handle(self, *args, **kwargs):
        users = Userdetails.objects.all()
        for user in users:
            if not user.password.startswith('pbkdf2_'):  
                plain_text_password = user.password
                user.set_password(plain_text_password)  
                user.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated passwords'))