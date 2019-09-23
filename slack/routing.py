# slack/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/slack/<str:room_name>/', consumers.SlackConsumer),
]