import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from authentication.models import User
from chat.models import Message


class ChatConsumer(WebsocketConsumer):
    pass
