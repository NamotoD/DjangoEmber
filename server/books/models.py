# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
  title       = models.CharField(max_length=500)
  author      = models.CharField(max_length=100)
  description = models.TextField()
