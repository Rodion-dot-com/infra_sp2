import os

from django.core.management.base import BaseCommand

from reviews.models import User


class Command(BaseCommand):
    help = 'Creates an admin user non-interactively'

    def handle(self, *args, **options):
        User.objects.create_superuser(
            username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
            email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
            password=os.getenv('DJANGO_SUPERUSER_PASSWORD')
        )
