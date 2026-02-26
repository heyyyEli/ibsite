# tok_planner/forms.py
from django import forms
from .models import TOKPrompt, TOKExhibitionPrompt, TOKObject

class EssayOutlineForm(forms.Form):
    prompt = forms.ModelChoiceField(queryset=TOKPrompt.objects.all(), required=False)
    intro = forms.CharField(widget=forms.Textarea, required=False)
    claim1 = forms.CharField(widget=forms.Textarea, required=False)
    counterclaim1 = forms.CharField(widget=forms.Textarea, required=False)
    claim2 = forms.CharField(widget=forms.Textarea, required=False)
    counterclaim2 = forms.CharField(widget=forms.Textarea, required=False)
    conclusion = forms.CharField(widget=forms.Textarea, required=False)

class CommentaryForm(forms.Form):
    exhibition_prompt = forms.ModelChoiceField(queryset=TOKExhibitionPrompt.objects.all())
    object_selected = forms.ModelChoiceField(queryset=TOKObject.objects.all())
    commentary_text = forms.CharField(widget=forms.Textarea, required=False)

class ReflectionForm(forms.Form):
    section = forms.ChoiceField(choices=[("essay", "Essay"), ("exhibition", "Exhibition")])
    content = forms.CharField(widget=forms.Textarea)