# tok_planner/views.py
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import (
    TOKPrompt, TOKEssayExemplar, TOKEssayOutline,
    TOKExhibitionPrompt, TOKObject, TOKExhibitionExemplar,
    TOKCommentary, TOKMilestone, TOKReflection
)
from .forms import EssayOutlineForm, CommentaryForm, ReflectionForm

# --- Dashboard ---
@login_required
def planner_dashboard(request):
    essay_milestones = TOKMilestone.objects.filter(student=request.user, section="essay")
    exhibition_milestones = TOKMilestone.objects.filter(student=request.user, section="exhibition")

    essay_progress = _progress_percent(essay_milestones)
    exhibition_progress = _progress_percent(exhibition_milestones)

    return render(request, "tok_planner/dashboard.html", {
        "essay_progress": essay_progress,
        "essay_progress_class": _progress_class(essay_progress),
        "exhibition_progress": exhibition_progress,
        "exhibition_progress_class": _progress_class(exhibition_progress),
    })

def _progress_percent(qs):
    total = qs.count() or 1
    completed = qs.filter(completed=True).count()
    return int((completed / total) * 100)

def _progress_class(progress):
    cls = (progress // 10) * 10
    return min(100, max(0, cls))

# --- Essay ---
@login_required
def prompt_list(request):
    year = timezone.now().year
    prompts = TOKPrompt.objects.filter(year=year).order_by("id") or TOKPrompt.objects.all()
    return render(request, "tok_planner/prompt_list.html", {"prompts": prompts, "year": year})

@login_required
def prompt_detail(request, pk):
    prompt = get_object_or_404(TOKPrompt, pk=pk)
    return render(request, "tok_planner/prompt_detail.html", {"prompt": prompt})

@login_required
def essay_exemplars(request):
    exemplars = TOKEssayExemplar.objects.all().order_by("title")
    return render(request, "tok_planner/essay_exemplars.html", {"exemplars": exemplars})

@login_required
def essay_outline(request):
    outline = TOKEssayOutline.objects.filter(student=request.user).last()
    initial = {}
    if outline:
        initial = {
            "prompt": outline.prompt_id,
            "intro": outline.intro,
            "claim1": outline.claim1,
            "counterclaim1": outline.counterclaim1,
            "claim2": outline.claim2,
            "counterclaim2": outline.counterclaim2,
            "conclusion": outline.conclusion,
        }
    form = EssayOutlineForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        if outline is None:
            outline = TOKEssayOutline.objects.create(student=request.user)
        outline.prompt = form.cleaned_data.get("prompt")
        outline.intro = form.cleaned_data.get("intro", "")
        outline.claim1 = form.cleaned_data.get("claim1", "")
        outline.counterclaim1 = form.cleaned_data.get("counterclaim1", "")
        outline.claim2 = form.cleaned_data.get("claim2", "")
        outline.counterclaim2 = form.cleaned_data.get("counterclaim2", "")
        outline.conclusion = form.cleaned_data.get("conclusion", "")
        outline.save()

        _generate_essay_milestones(request.user)
        return redirect("tok_essay_outline")

    return render(request, "tok_planner/essay_outline.html", {"form": form})

def _generate_essay_milestones(user):
    # Simple plan over ~6 weeks from today
    today = timezone.now().date()
    milestones = [
        ("Prompt selection", today + timedelta(days=3)),
        ("Outline draft", today + timedelta(days=10)),
        ("First essay draft", today + timedelta(days=24)),
        ("Supervisor feedback", today + timedelta(days=30)),
        ("Final essay submission", today + timedelta(days=42)),
    ]
    _upsert_milestones(user, "essay", milestones)

# --- Exhibition ---
@login_required
def exhibition_prompt_list(request):
    prompts = TOKExhibitionPrompt.objects.all().order_by("id")
    return render(request, "tok_planner/exhibition_prompt_list.html", {"prompts": prompts})

@login_required
def object_list(request):
    objects = TOKObject.objects.all().order_by("name")
    return render(request, "tok_planner/object_list.html", {"objects": objects})

@login_required
def exhibition_exemplars(request):
    exemplars = TOKExhibitionExemplar.objects.all().order_by("title")
    return render(request, "tok_planner/exhibition_exemplars.html", {"exemplars": exemplars})

@login_required
def exhibition_commentary(request):
    latest = TOKCommentary.objects.filter(student=request.user).last()
    initial = {}
    if latest:
        initial = {
            "exhibition_prompt": latest.exhibition_prompt_id,
            "object_selected": latest.object_selected_id,
            "commentary_text": latest.commentary_text,
        }
    form = CommentaryForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        if latest is None:
            latest = TOKCommentary.objects.create(student=request.user)
        latest.exhibition_prompt = form.cleaned_data["exhibition_prompt"]
        latest.object_selected = form.cleaned_data["object_selected"]
        latest.commentary_text = form.cleaned_data.get("commentary_text", "")
        latest.save()

        _generate_exhibition_milestones(request.user)
        return redirect("tok_exhibition_commentary")

    return render(request, "tok_planner/exhibition_commentary.html", {"form": form})

def _generate_exhibition_milestones(user):
    today = timezone.now().date()
    milestones = [
        ("Object selection", today + timedelta(days=3)),
        ("Draft commentary", today + timedelta(days=10)),
        ("Rehearsal", today + timedelta(days=20)),
        ("Final presentation", today + timedelta(days=30)),
    ]
    _upsert_milestones(user, "exhibition", milestones)

# --- Shared: Reflections ---
@login_required
def reflections(request):
    form = ReflectionForm(request.POST or None)
    reflections = TOKReflection.objects.filter(student=request.user).order_by("-date")
    if request.method == "POST" and form.is_valid():
        TOKReflection.objects.create(
            student=request.user,
            section=form.cleaned_data["section"],
            content=form.cleaned_data["content"],
        )
        return redirect("tok_reflections")

    return render(request, "tok_planner/reflections.html", {"form": form, "reflections": reflections})

# ---presentation---
@login_required
def presentation_prep(request):
    return render(request, "tok_planner/presentation_prep.html")


# --- Helpers ---
def _upsert_milestones(user, section, items):
    for title, due in items:
        obj, created = TOKMilestone.objects.get_or_create(
            student=user, section=section, title=title,
            defaults={"due_date": due, "completed": False}
        )
        if not created:
            obj.due_date = due
            obj.save()


