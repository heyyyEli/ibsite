# cas_idea_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.idea_list, name="cas_idea_list"),
]