# cas_idea_generator/views.py
from django.shortcuts import render
from .models import CASIdea

def idea_list(request):
    query = request.GET.get("q", "")
    impact = request.GET.get("impact", "")
    skill = request.GET.get("skill", "")

    ideas = CASIdea.objects.all()
    if query:
        ideas = ideas.filter(title__icontains=query)
    if impact:
        ideas = ideas.filter(impact_area__icontains=impact)
    if skill:
        ideas = ideas.filter(skills__icontains=skill)

    return render(request, "cas_idea_generator/idea_list.html", {"ideas": ideas})
