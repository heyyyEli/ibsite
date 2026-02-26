
from django.db import models

class CASIdea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creativity = models.BooleanField(default=False)
    activity = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    duration_months = models.PositiveIntegerField(default=1)
    group_size = models.CharField(max_length=100, help_text="e.g. 4-6 students")
    impact_area = models.CharField(max_length=100, help_text="e.g. Environment, Health, Arts")
    skills = models.CharField(max_length=200, help_text="Comma-separated skills like leadership, design, teamwork")
    tags = models.CharField(max_length=200, help_text="Keywords for filtering")

    def __str__(self):
        return self.title
    