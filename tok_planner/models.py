# tok_planner/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# --- TOK Essay ---
class TOKPrompt(models.Model):
    year = models.IntegerField()
    prompt_text = models.TextField()
    key_terms = models.TextField(blank=True)
    interpretations = models.TextField(blank=True)
    guiding_questions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.year} - {self.prompt_text[:60]}"

class TOKEssayExemplar(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="tok_essay_exemplars/")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Student outline storage (optional, can skip if you only render form)
class TOKEssayOutline(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.ForeignKey(TOKPrompt, on_delete=models.SET_NULL, null=True, blank=True)
    intro = models.TextField(blank=True)
    claim1 = models.TextField(blank=True)
    counterclaim1 = models.TextField(blank=True)
    claim2 = models.TextField(blank=True)
    counterclaim2 = models.TextField(blank=True)
    conclusion = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Outline by {self.student} ({self.prompt_id})"

# --- TOK Exhibition ---
class TOKExhibitionPrompt(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:60]

class TOKObject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="tok_objects/", blank=True, null=True)

    def __str__(self):
        return self.name

class TOKExhibitionExemplar(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="tok_exhibition_exemplars/")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

class TOKCommentary(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exhibition_prompt = models.ForeignKey(TOKExhibitionPrompt, on_delete=models.SET_NULL, null=True)
    object_selected = models.ForeignKey(TOKObject, on_delete=models.SET_NULL, null=True)
    commentary_text = models.TextField(blank=True)  # ~950 words
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commentary by {self.student}"

# --- Shared: Milestones & Reflections ---
class TOKMilestone(models.Model):
    SECTION_CHOICES = [("essay", "Essay"), ("exhibition", "Exhibition")]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.section} - {self.title}"

class TOKReflection(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.CharField(max_length=20, choices=[("essay", "Essay"), ("exhibition", "Exhibition")])
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Reflection by {self.student} ({self.section})"