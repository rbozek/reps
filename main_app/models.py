from django.db import models
from django.urls import reverse
from datetime import datetime


class Category(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('category-detail', kwargs={'pk': self.id})


class Rep(models.Model):
  name = models.CharField(max_length=100)
  time_spent = models.IntegerField()
  description = models.TextField(max_length=500)
  rep_date_time = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  # created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
  updated = models.DateTimeField(auto_now=True)
  # updated = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
  categories = models.ManyToManyField(Category)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('rep-detail', kwargs={'rep_id': self.id})