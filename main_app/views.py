from django.shortcuts import render

#RB Step 1, for home view
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>We\'re gonna get some reps!</h1>')