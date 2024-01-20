from django.core.management import BaseCommand

from users.models import User

email = 'admin@admin.admin'
password = 'admin'


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=email,
            is_superuser=True,
            is_staff=True,
        )
        user.set_password(password)
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Admin user created'))
        self.stdout.write(self.style.SUCCESS(f'email: {email}'))
        self.stdout.write(self.style.SUCCESS(f'password: {password}'))
