from django.core.management.base import BaseCommand
from ...models import CustomUser


class Command(BaseCommand):
    help = 'Create initial teacher accounts'

    def handle(self, *args, **kwargs):
        teachers = [
            {"username": "EnglishA", "role": "teacher", "password": "TempPass123"},
            {"username": "MathHL",  "role": "teacher", "password": "TempPass456"},
            {"username": "Biology", "role": "teacher", "password": "TempPass789"},
            {"username": "Physics",  "role": "teacher", "password": "T123"},
            {"username": "MathSL",  "role": "teacher", "password": "T456"},
            {"username": "Chemistry",  "role": "teacher", "password": "T789"},
            {"username": "Business",  "role": "teacher", "password": "Te123"},
            {"username": "Psychology",  "role": "teacher", "password": "Te456"},
            {"username": "Digital Society",  "role": "teacher", "password": "Te789"},
            {"username": "Computer Science",  "role": "teacher", "password": "Teach123"},
            {"username": "Art",  "role": "teacher", "password": "Teach456"},
            {"username": "Spanish",  "role": "teacher", "password": "Teach789"},
            {"username": "French",  "role": "teacher", "password": "TE123"},
            {"username": "German",  "role": "teacher", "password": "TE456"},
            {"username": "CAS",  "role": "teacher", "password": "TE789"},
        ]   
        for data in teachers:
            if not CustomUser.objects.filter(username=data["username"]).exists():
                user = CustomUser.objects.create_user(
                    username=data["username"],
                    password=data["password"],
                    role="teacher",
                    is_staff=True,  # allow admin access if needed
                    is_active=True,
                )
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Teacher user {data["username"]} created.'))
            else:
                self.stdout.write(f'Teacher {data["username"]} already exists.')
