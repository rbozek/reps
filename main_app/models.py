from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User


class Category(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=25, null=True, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('category-detail', kwargs={'pk': self.id})


class Rep(models.Model):
  name = models.CharField(max_length=100)
  time_spent = models.IntegerField('Time spent (mins):', null=True, blank=True)
  # ice-box: add 'time' back in
  # rep_date_time = models.DateTimeField('Date & time:', null=True, blank=True)
  rep_date_time = models.DateField('Date:', null=True, blank=True)
  description = models.TextField(max_length=500, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  categories = models.ManyToManyField(Category, blank=True)
  # RB Auth - linking Rep to User
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('rep-detail', kwargs={'rep_id': self.id})
  
  # for sorting - have not tested yet
  # class Meta:
  #   ordering = ['-rep_date_time']