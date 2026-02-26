# tok_planner/admin.py
from django.contrib import admin
from .models import (
    TOKPrompt, TOKEssayExemplar, TOKEssayOutline,
    TOKExhibitionPrompt, TOKObject, TOKExhibitionExemplar,
    TOKCommentary, TOKMilestone, TOKReflection
)

@admin.register(TOKPrompt)
class TOKPromptAdmin(admin.ModelAdmin):
    list_display = ("year", "prompt_text")
    list_filter = ("year",)
    search_fields = ("prompt_text",)

@admin.register(TOKEssayExemplar)
class TOKEssayExemplarAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(TOKEssayOutline)
class TOKEssayOutlineAdmin(admin.ModelAdmin):
    list_display = ("student", "prompt", "updated_at")
    list_filter = ("updated_at",)

@admin.register(TOKExhibitionPrompt)
class TOKExhibitionPromptAdmin(admin.ModelAdmin):
    list_display = ("text",)
    search_fields = ("text",)

@admin.register(TOKObject)
class TOKObjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(TOKExhibitionExemplar)
class TOKExhibitionExemplarAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(TOKCommentary)
class TOKCommentaryAdmin(admin.ModelAdmin):
    list_display = ("student", "exhibition_prompt", "object_selected", "updated_at")

@admin.register(TOKMilestone)
class TOKMilestoneAdmin(admin.ModelAdmin):
    list_display = ("student", "section", "title", "due_date", "completed")
    list_filter = ("section", "completed")

@admin.register(TOKReflection)
class TOKReflectionAdmin(admin.ModelAdmin):
    list_display = ("student", "section", "date")
    list_filter = ("section", "date")