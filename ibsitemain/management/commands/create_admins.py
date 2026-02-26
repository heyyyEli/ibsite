from django.core.management.base import BaseCommand
from ...models import CustomUser


class Command(BaseCommand):
    help = 'Create initial admin accounts'

    def handle(self, *args, **kwargs):
        admins = [
            {"username": "ibcoordinator", "email": "fatehi.tisibdp@gmail.com", "password": "AdminPass123"},
            {"username": "admin2", "email": "admin2@example.com", "password": "AdminPass123"},
            {"username": "admin3", "email": "admin3@example.com", "password": "AdminPass123"},
            {"username": "admin4", "email": "admin4@example.com", "password": "AdminPass123"},
        ]
        for data in admins:
            if not CustomUser.objects.filter(username=data["username"]).exists():
                user = CustomUser.objects.create_superuser(
                    username=data["username"],
                    email=data["email"],
                    password=data["password"],
                    role='admin',
                )
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Admin {data["username"]} created.'))
            else:
                self.stdout.write(f'Admin {data["username"]} already exists.')
