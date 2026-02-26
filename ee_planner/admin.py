# ee_planner/admin.py
from django.contrib import admin
from .models import SubjectStats, Exemplar, EEProject, Milestone

@admin.register(SubjectStats)
class SubjectStatsAdmin(admin.ModelAdmin):
    list_display = ("subject",)

@admin.register(Exemplar)
class ExemplarAdmin(admin.ModelAdmin):
    list_display = ("subject", "title")

class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 0

@admin.register(EEProject)
class EEProjectAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "topic", "start_date", "deadline")
    inlines = [MilestoneInline]
