# 

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from message.models import Message

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        # self.room_name = "global"  #default room
        self.room_name = self.scope['url_route']['kwargs']['room_name']    # multiple room
        self.room_group_name = f"chat_{self.room_name}"

        if self.scope["user"].is_anonymous:
            await self.close()

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data):

        data = json.loads(text_data)
        message = data['message']
        user = self.scope["user"]

        msg = await self.save_message(user, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg.content,
                'username': user.email,
                'timestamp': str(msg.timestamp)
            }
        )

    async def chat_message(self, event):

        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'timestamp': event['timestamp']
        }))
        
     #save to database
    async def save_message(self, user, message):
        return await Message.objects.acreate(
            sender=user,
            room=self.room_name,
            content=message
        )