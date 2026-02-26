# chat/urls.py
from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.chat_home, name="home"),
    path("channel/<str:channel_name>/", views.channel_messages, name="channel_messages"),
    path("unread/", views.unread_counts, name="unread_counts"),

]