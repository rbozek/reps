from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.db.models.functions import Lower

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Rep, Category

#RB Auth:
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')


@login_required
def rep_index(request):
  # 2 ways of accessing just User's reps:
  # reps = request.user.rep_set.all()
  reps = Rep.objects.filter(user=request.user).order_by('-rep_date_time')
  return render(request, 'reps/index.html', { 'reps': reps })

@login_required
def rep_detail(request, rep_id):
  rep = Rep.objects.get(id=rep_id)
  return render(request, 'reps/detail.html', { 'rep': rep })


class RepCreate(LoginRequiredMixin, CreateView):
  model = Rep
  fields = ['name', 'time_spent', 'rep_date_time', 'description', 'categories']
  success_url = '/reps/'
  #RB Auth: called when valid form
  def form_valid(self, form):
    # Assign logged-in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the rep
    # continue w CreateView as usual
    return super().form_valid(form)

class RepUpdate(LoginRequiredMixin, UpdateView):
  model = Rep
  fields = '__all__'
  # can specify specific fields if there's something we dont want to allow edit
  # fields = ['category', 'time_spent', 'description']

class RepDelete(LoginRequiredMixin, DeleteView):
  model = Rep
  success_url = '/reps/'



class CategoryCreate(LoginRequiredMixin, CreateView):
  model = Category
  fields = '__all__'
  def get_success_url(self):
    return reverse_lazy('category-index')

def category_list(request):
    categories = Category.objects.filter(user=request.user).order_by(Lower('name'))
    # categories = Category.objects.all().order_by(Lower('name'))
    return render(request, 'categories/category_list.html', {'category_list': categories})
    # return render(request, 'main-app/category_list.html', {'category_list': categories})
    # return render(request, 'category_list.html', {'category_list': categories})

# class CategoryList(LoginRequiredMixin, ListView):
#   model = Category


class CategoryDetail(LoginRequiredMixin, DetailView):
  model = Category

class CategoryUpdate(LoginRequiredMixin, UpdateView):
  model = Category
  fields = '__all__'
  # fields = ['name', 'color']
  def get_success_url(self):
    return reverse_lazy('category-index')

class CategoryDelete(LoginRequiredMixin, DeleteView):
  model = Category
  success_url = '/categories/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Create 'user' form object that includes data from browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Add the user to the database
      user = form.save()
      # To log a user in
      login(request, user)
      return redirect('rep-index')
    else:
      error_message = 'Invalid sign up - try again'
  # If there is a GET request, or a BAD POST req, render signup.html with empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})