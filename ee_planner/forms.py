# ee_planner/forms.py
from django import forms

SUBJECT_CHOICES = [
    ("Biology", "Biology"),
    ("Chemistry", "Chemistry"),
    ("Physics", "Physics"),
    ("Psychology", "Psychology"),
    ("Business", "Business"),
    ("English Language and Literature A", "English language and Literature A"),
    ("Persian A", "Persian A"),

]

class BrainstormForm(forms.Form):
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    broad_interest = forms.CharField(max_length=200, help_text="e.g., social media, climate change, Renaissance art")

class TimelineForm(forms.Form):
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    topic = forms.CharField(max_length=200)
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))