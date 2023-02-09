import os

from django.core.management.base import BaseCommand
from reviews.models import User


class Command(BaseCommand):
    help = 'Creates an admin user non-interactively if no users exist'

    def handle(self, *args, **options):
        if User.objects.count() != 0:
            self.stderr.write('Superuser can only be initialized if no users '
                              'exist')
            return
        if all(var in os.environ for var in (
                'DJANGO_SUPERUSER_USERNAME',
                'DJANGO_SUPERUSER_EMAIL',
                'DJANGO_SUPERUSER_PASSWORD'
        )):
            User.objects.create_superuser(
                username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
                email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
                password=os.getenv('DJANGO_SUPERUSER_PASSWORD')
            )
            self.stdout.write('Superuser created successfully.')
        else:
            self.stderr.write('The creation was skipped, make sure you added '
                              'all the necessary variables to the '
                              'environment file')
