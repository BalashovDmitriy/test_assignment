from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.admin',
            is_superuser=True,
            is_staff=True,
        )
        user.set_password('admin')
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Admin user created'))
        self.stdout.write(self.style.SUCCESS(f'user: admin@admin.admin'))
        self.stdout.write(self.style.SUCCESS(f'password: admin'))
