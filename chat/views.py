# chat/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Channel, Message, ChannelVisit
from .utils import format_user_display

@login_required
def chat_home(request):
    channels = Channel.objects.all().order_by("name")
    # Track visits for unread indicators
    for ch in channels:
        ChannelVisit.objects.get_or_create(user=request.user, channel=ch, defaults={"last_visited": now()})
    return render(request, "chat/chat_home.html", {"channels": channels})

@login_required
def channel_messages(request, channel_name):
    channel = get_object_or_404(Channel, name=channel_name)
    messages = Message.objects.filter(channel=channel).select_related("user").order_by("timestamp")
    # Update visit for unread reset
    ChannelVisit.objects.update_or_create(
        user=request.user, channel=channel, defaults={"last_visited": now()}
    )
    formatted = [
        {
            "display_name": format_user_display(m.user),
            "content": m.content,
            "timestamp": m.timestamp,
        } for m in messages
    ]
    return render(request, "chat/partials/messages_list.html", {"messages": formatted, "channel": channel})


from django.http import JsonResponse

@login_required
def unread_counts(request):
    counts = {}
    for ch in Channel.objects.all():
        last_visit = ChannelVisit.objects.filter(user=request.user, channel=ch).first()
        latest = Message.objects.filter(channel=ch).order_by("-timestamp").first()
        if latest and last_visit:
            counts[ch.name] = 1 if latest.timestamp > last_visit.last_visited else 0
        else:
            counts[ch.name] = 0
    return JsonResponse(counts)

# chat/views.py
from django.contrib.auth.decorators import login_required