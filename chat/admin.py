from django.contrib import admin
# chat/admin.py
from .models import Channel, Message, ChannelVisit
admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(ChannelVisit)

# Register your models here.
