from django.core.management import BaseCommand
import os
from users.models import User

email_password = os.environ.get("EMAILHOSTPASSWORD")


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='a@ru.ru',
            first_name='Mer1d1an',
            last_name='Nikita',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password(email_password)
        user.save()
