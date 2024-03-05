from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  
  path('reps/', views.rep_index, name='rep-index'),
  path('reps/<int:rep_id>', views.rep_detail, name='rep-detail'),
  path('reps/create', views.RepCreate.as_view(), name='rep-create'),
  path('reps/<int:pk>/update/', views.RepUpdate.as_view(), name='rep-update'),
  path('reps/<int:pk>/delete/', views.RepDelete.as_view(), name='rep-delete'),

  path('categories/create/', views.CategoryCreate.as_view(), name='category-create'),
  path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
  path('categories/', views.CategoryList.as_view(), name='category-index'),
]