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

from .models import Rep, Category, Photo
#AWS photo svc:
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'reps-app'

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
  # this chunk is to prevent non-user categories from appearing:
  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['categories'].queryset = form.fields['categories'].queryset.filter(user=self.request.user)
    return form

class RepUpdate(LoginRequiredMixin, UpdateView):
  model = Rep
  fields = ['name', 'time_spent', 'rep_date_time', 'description', 'categories']
  # this chunk is to prevent non-user categories from appearing:
  def get_form(self, form_class=None):
    form = super().get_form(form_class)
    form.fields['categories'].queryset = form.fields['categories'].queryset.filter(user=self.request.user)
    return form

class RepDelete(LoginRequiredMixin, DeleteView):
  model = Rep
  success_url = '/reps/'



def category_list(request):
    categories = Category.objects.filter(user=request.user).order_by(Lower('name'))
    # categories = Category.objects.all().order_by(Lower('name'))
    return render(request, 'main_app/category_list.html', {'category_list': categories})

# class CategoryList(LoginRequiredMixin, ListView):
#   model = Category

class CategoryCreate(LoginRequiredMixin, CreateView):
  model = Category
  fields = ['name', 'color']
  #RB Auth: called when valid form
  def form_valid(self, form):
    # Assign logged-in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the rep
    # continue w CreateView as usual
    return super().form_valid(form)
  def get_success_url(self):
    return reverse_lazy('category-index')
  

class CategoryDetail(LoginRequiredMixin, DetailView):
  model = Category

class CategoryUpdate(LoginRequiredMixin, UpdateView):
  model = Category
  fields = ['name', 'color']
  # fields = '__all__'
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

def add_photo(request, rep_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to rep_id or rep (if you have a rep object)
      photo = Photo(url=url, rep_id=rep_id)
      # Remove old photo if it exists
      rep_photo = Photo.objects.filter(rep_id=rep_id)
      if rep_photo.first():
        rep_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('rep-detail', rep_id=rep_id)