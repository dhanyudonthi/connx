from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from unified_communications.models import UserProfile

class Command(BaseCommand):
    help = 'Create a new admin user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='varshini').exists():
            user = User.objects.create_superuser('varshini', 'varshini@test.com', 'Admin@123')
            UserProfile.objects.create(user=user, user_level=UserProfile.INTERNAL)  # Set user level to INTERNAL
            self.stdout.write(self.style.SUCCESS('Successfully created new admin user'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
