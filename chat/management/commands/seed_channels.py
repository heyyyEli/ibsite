# chat/management/commands/seed_channels.py
from django.core.management.base import BaseCommand
from chat.models import Channel

DEFAULTS = [
    "general", "ee", "tok", "cas",
    "language_literature", "language_acquisition",
    "individuals_societies", "sciences", "mathematics", "arts",
]

class Command(BaseCommand):
    help = "Seed default chat channels"

    def handle(self, *args, **kwargs):
        created = 0
        for name in DEFAULTS:
            Channel.objects.get_or_create(name=name)
            created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} channels."))