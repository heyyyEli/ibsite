# ee_planner/views.py
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import SubjectStats, Exemplar, EEProject, Milestone
from .forms import BrainstormForm, TimelineForm

@login_required
def planner_dashboard(request):
    projects = EEProject.objects.filter(student=request.user).order_by("-start_date")
    return render(request, "ee_planner/dashboard.html", {"projects": projects})

@login_required
def brainstorm(request):
    suggestions = []
    stats = None
    exemplars = []
    form = BrainstormForm(request.GET or None)
    if form.is_valid():
        subject = form.cleaned_data["subject"]
        broad_interest = form.cleaned_data["broad_interest"]

        # simple suggestion engine demo (replace with richer logic later)
        suggestions = [
            f"Refine: Narrow {broad_interest} within {subject} to a specific time/place/case.",
            f"Method: Identify 2–3 key sources or datasets relevant to {broad_interest}.",
            f"Question: 'To what extent did {broad_interest} influence X within {subject} context?'",
        ]

        stats = SubjectStats.objects.filter(subject=subject).first()
        exemplars = Exemplar.objects.filter(subject=subject)

    return render(
        request,
        "ee_planner/brainstorm.html",
        {"form": form, "suggestions": suggestions, "stats": stats, "exemplars": exemplars},
    )

@login_required
def create_timeline(request):
    form = TimelineForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        subject = form.cleaned_data["subject"]
        topic = form.cleaned_data["topic"]
        start_date = form.cleaned_data["start_date"]
        deadline = form.cleaned_data["deadline"]

        project = EEProject.objects.create(
            student=request.user, subject=subject, topic=topic,
            start_date=start_date, deadline=deadline
        )
        _generate_milestones(project)
        return redirect("ee_timeline_detail", project_id=project.id)

    # default start date today
    if request.method == "GET":
        form.initial["start_date"] = timezone.now().date()

    return render(request, "ee_planner/create_timeline.html", {"form": form})

@login_required
@login_required
def timeline_detail(request, project_id):
    project = get_object_or_404(EEProject, id=project_id, student=request.user)
    milestones = project.milestones.all()

    # Calculate progress
    completed = milestones.filter(completed=True).count()
    total = milestones.count() or 1
    progress = int((completed / total) * 100)

    # Round to nearest 10 for CSS class
    progress_class = (progress // 10) * 10
    if progress_class > 100:
        progress_class = 100

    return render(
        request,
        "ee_planner/timeline_detail.html",
        {
            "project": project,
            "milestones": milestones,
            "progress": progress,          # for text display
            "progress_class": progress_class,  # for CSS class
        }
    )

def _generate_milestones(project: EEProject):
    # naive phased plan; adjust to fit your school’s calendar
    sd, dl = project.start_date, project.deadline
    total_days = (dl - sd).days
    if total_days < 45:
        # compressed schedule
        phases = [
            ("Proposal submission", sd + timedelta(days=10)),
            ("Research notes & sources", sd + timedelta(days=20)),
            ("First draft", sd + timedelta(days=35)),
            ("Supervisor meeting", sd + timedelta(days=40)),
            ("Final draft & revisions", dl - timedelta(days=7)),
            ("Proofreading & formatting", dl - timedelta(days=3)),
        ]
    else:
        # standard schedule (~5–6 months)
        phases = [
            ("Proposal submission", sd + timedelta(days=14)),
            ("Research notes & sources", sd + timedelta(days=45)),
            ("First draft", sd + timedelta(days=75)),
            ("Supervisor meeting 1", sd + timedelta(days=30)),
            ("Supervisor meeting 2", sd + timedelta(days=60)),
            ("Supervisor meeting 3", sd + timedelta(days=90)),
            ("Final draft & revisions", dl - timedelta(days=14)),
            ("Proofreading & formatting", dl - timedelta(days=5)),
        ]

    for idx, (title, due) in enumerate(phases, start=1):
        Milestone.objects.create(timeline=project, title=title, due_date=due, order=idx)
