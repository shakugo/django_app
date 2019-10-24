# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import json

from django.views.generic import View
# Create your views here.
def index(request):
    return render(request, 'slack/index.html', {})

def room(request, room_name):
    return render(request, 'slack/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

#ログイン機能
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('../')
        return render(request, 'slack/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'slack/login.html', {'form': form,})

account_login = Account_login.as_view()
