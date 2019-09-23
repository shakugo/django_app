# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request):
    return render(request, 'slack/index.html', {})

def room(request, room_name):
    return render(request, 'slack/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
