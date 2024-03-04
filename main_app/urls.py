from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('reps/', views.rep_index, name='rep-index'),
  path('reps/<int:rep_id>', views.rep_detail, name='rep-detail'),
  path('reps/create', views.RepCreate.as_view(), name='rep-create'),
]