# ee_planner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.planner_dashboard, name="ee_dashboard"),
    path("brainstorm/", views.brainstorm, name="ee_brainstorm"),
    path("timeline/create/", views.create_timeline, name="ee_create_timeline"),
    path("timeline/<int:project_id>/", views.timeline_detail, name="ee_timeline_detail"),
]