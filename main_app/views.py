from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Rep, Category

#RB Step 1, for home view - unused now that we re-defined
# from django.http import HttpResponse

#RB Step 2, temp store model here
# class Rep:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, category, timespent, description, timestamp):
#     self.name = name
#     self.category = category
#     self.timespent = timespent
#     self.description = description
#     self.timestamp = timestamp

# reps = [
#   Rep('Practiced piano', 'Music', '30mins', 'Practiced scales & chords in 12 keys.', 'Tues 3 pm'),
#   Rep('Practiced guitar', 'Music', '45mins', 'Practiced songs for lessons.', 'Fri 10 am'),
#   Rep('Do some coding challenges', 'Coding', '1hr', 'Started working thru HackerRank challenges.', 'Mon 12 pm'),
# ]



# def home(request):
#   return render(request, 'home.html')
#RB Auth:
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def rep_index(request):
  reps = Rep.objects.all()
  return render(request, 'reps/index.html', { 'reps': reps })

def rep_detail(request, rep_id):
  rep = Rep.objects.get(id=rep_id)
  return render(request, 'reps/detail.html', { 'rep': rep })

class RepCreate(CreateView):
  model = Rep
  fields = '__all__'
  # fields = ['name', 'category', 'time_spent', 'description']
  success_url = '/reps/'

class RepUpdate(UpdateView):
  model = Rep
  fields = '__all__'
  # can specify specific fields if there's something we dont want to allow edit
  # fields = ['category', 'time_spent', 'description']

class RepDelete(DeleteView):
  model = Rep
  success_url = '/reps/'



class CategoryCreate(CreateView):
  model = Category
  fields = '__all__'

class CategoryList(ListView):
  model = Category

class CategoryDetail(DetailView):
  model = Category

class CategoryUpdate(UpdateView):
  model = Category
  fields = '__all__'
  # fields = ['name', 'color']

class CategoryDelete(DeleteView):
  model = Category
  success_url = '/categories/'