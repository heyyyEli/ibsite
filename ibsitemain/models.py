

# Creating models for user here .

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta




class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    full_name = models.CharField(max_length=150, blank=True)
    graduation_year = models.PositiveIntegerField(null=True, blank=True)
    enrollment_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now) 

 

    def save(self, *args, **kwargs):
        if self.role == 'student' and self.enrollment_date and not self.expiry_date:
            self.expiry_date = self.enrollment_date + timedelta(days=365*2)  # 2 years expiry
        super().save(*args, **kwargs)

    def is_account_active(self):
        if self.role == 'student' and self.expiry_date:
            return timezone.now().date() <= self.expiry_date
        return True  # teachers/admins always active by default
    





class NewsItem(models.Model):
    CATEGORY_CHOICES = [
        ('community', 'Community'),
        ('resources', 'Resources'),
        ('cas', 'CAS'),
        ('headlines', 'Headlines'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    attachment = models.FileField(upload_to='news_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"




class Subject(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=100)  # Grouping by your categories like Language A, Sciences, etc.

    def __str__(self):
        return self.name




class CASProject(models.Model):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    creativity = models.BooleanField(default=False)
    activity = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    duration = models.CharField(max_length=100, help_text="e.g. 3 months")
    impact = models.CharField(max_length=200, help_text="e.g. Raised funds, supported shelters")
    image = models.ImageField(upload_to="cas_projects/", blank=True, null=True)

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return f"{self.title} ({self.year})"


