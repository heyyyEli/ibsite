# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from django.utils.timezone import now
from .models import Channel, Message, ChannelVisit

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_name_key = self.scope["url_route"]["kwargs"]["channel_name"]
        self.group = f"chat_{self.channel_name_key}"
        await self.channel_layer.group_add(self.group, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        user = self.scope.get("user", AnonymousUser())
        data = json.loads(text_data)
        content = data.get("message", "").strip()
        if not content or not user.is_authenticated:
            return
        # Persist to DB
        channel = await self._get_channel(self.channel_name_key)
        await self._save_message(channel, user, content)
        # Broadcast
        await self.channel_layer.group_send(
            self.group,
            {
                "type": "chat_message",
                "user": user.first_name or user.username,
                "year": "IBDP1" if getattr(user, "dp_year", None) == 1 else "IBDP2",
                "content": content,
                "timestamp": now().strftime("%H:%M"),
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group, self.channel_name)

    @staticmethod
    async def _get_channel(name):
        return await Channel.objects.aget(name=name)

    @staticmethod
    async def _save_message(channel, user, content):
        await Message.objects.acreate(channel=channel, user=user, content=content)
        await ChannelVisit.objects.aupdate_or_create(
            user=user, channel=channel, defaults={"last_visited": now()}
        )