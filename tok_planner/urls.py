# tok_planner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner_dashboard, name='tok_dashboard'),

    # Essay
    path('essay/prompts/', views.prompt_list, name='tok_prompt_list'),
    path('essay/prompts/<int:pk>/', views.prompt_detail, name='tok_prompt_detail'),
    path('essay/exemplars/', views.essay_exemplars, name='tok_essay_exemplars'),
    path('essay/outline/', views.essay_outline, name='tok_essay_outline'),

    # Exhibition
    path('exhibition/prompts/', views.exhibition_prompt_list, name='tok_exhibition_prompt_list'),
    path('exhibition/objects/', views.object_list, name='tok_object_list'),
    path('exhibition/exemplars/', views.exhibition_exemplars, name='tok_exhibition_exemplars'),
    path('exhibition/commentary/', views.exhibition_commentary, name='tok_exhibition_commentary'),
    path('exhibition/presentation/', views.presentation_prep, name='tok_presentation_prep'),

    # Shared
    path('reflections/', views.reflections, name='tok_reflections'),
]