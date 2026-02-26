# chat/models.py
from django.db import models
from django.conf import settings

class Channel(models.Model):
    SUBJECT_GROUPS = [
        ("general", "General"),
        ("ee", "Extended Essay"),
        ("tok", "Theory of Knowledge"),
        ("cas", "CAS"),
        ("language_literature", "Group 1: Language & Literature"),
        ("language_acquisition", "Group 2: Language Acquisition"),
        ("individuals_societies", "Group 3: Individuals & Societies"),
        ("sciences", "Group 4: Sciences"),
        ("mathematics", "Group 5: Mathematics"),
        ("arts", "Group 6: The Arts"),
    ]
    name = models.CharField(max_length=50, choices=SUBJECT_GROUPS, unique=True)

    def __str__(self):
        return self.get_name_display()

class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} in {self.channel.name} at {self.timestamp}"

class ChannelVisit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    last_visited = models.DateTimeField()

    class Meta:
        unique_together = ("user", "channel")

    def __str__(self):
        return f"{self.user.username} visited {self.channel.name} at {self.last_visited}"

