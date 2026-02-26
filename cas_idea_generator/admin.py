# cas_idea_generator/admin.py
from django.contrib import admin
from .models import CASIdea

@admin.register(CASIdea)
class CASIdeaAdmin(admin.ModelAdmin):
    list_display = ("title", "impact_area", "duration_months", "group_size")
    list_filter = ("creativity", "activity", "service", "impact_area")
    search_fields = ("title", "description", "skills", "tags")
