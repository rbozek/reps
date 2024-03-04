from django.db import models
from datetime import datetime


class Rep(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  timespent = models.IntegerField()
  description = models.TextField(max_length=500)
  created = models.DateTimeField(auto_now_add=True)
  # created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
  updated = models.DateTimeField(auto_now=True)
  # updated = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

  def __str__(self):
    return self.name