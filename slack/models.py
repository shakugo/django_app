# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ChatLog(models.Model):
  message = models.TextField()
  send_date = models.DateTimeField()
