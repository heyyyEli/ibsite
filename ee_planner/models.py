# ee_planner/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SubjectStats(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    avg_grade_distribution = models.JSONField(default=dict)  # {"A": 15, "B": 40, "C": 30, "D": 10, "E": 5}
    difficulty_notes = models.TextField(blank=True)
    common_pitfalls = models.TextField(blank=True)

    def __str__(self):
        return f"{self.subject} stats"

class Exemplar(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="exemplars/")  # ensure MEDIA settings configured

    def __str__(self):
        return f"{self.subject} - {self.title}"

class EEProject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    start_date = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.topic}"

class Milestone(models.Model):
    timeline = models.ForeignKey(EEProject, on_delete=models.CASCADE, related_name="milestones")
    title = models.CharField(max_length=120)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)  # for sorted display

    class Meta:
        ordering = ["order", "due_date"]

    def __str__(self):
        return f"{self.title} ({self.due_date})"