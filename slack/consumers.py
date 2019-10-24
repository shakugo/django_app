# slack/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from channels.db import database_sync_to_async
import datetime
from slack.models import ChatLog
import pytz

class SlackConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'init': 1,
            'message': self.get_message()
        }))


        self.messages = self.get_message()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.save_message(message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message
            }
        )

    # Receive message from room group
    def send_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def send_log_messages(self, event):
        message = event['text']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))


    #@database_sync_to_async
    def save_message(self, message):
        dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        now = dt_now.strftime("%s")
        ChatLog.objects.create(
            message = message,
            send_date = dt_now,
        )
        # return User.objects.all()[0].name

    def get_message(self):
        return list(ChatLog.objects.values_list('message'))

