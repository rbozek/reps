from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),

  path('accounts/signup/', views.signup, name='signup'),

  path('reps/', views.rep_index, name='rep-index'),
  path('reps/<int:rep_id>', views.rep_detail, name='rep-detail'),
  path('reps/create', views.RepCreate.as_view(), name='rep-create'),
  path('reps/<int:pk>/update/', views.RepUpdate.as_view(), name='rep-update'),
  path('reps/<int:pk>/delete/', views.RepDelete.as_view(), name='rep-delete'),
  path('reps/<int:rep_id>/add-photo/', views.add_photo, name='add-photo'),

  path('categories/create/', views.CategoryCreate.as_view(), name='category-create'),
  path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
  path('categories/', views.category_list, name='category-index'),
  path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
  path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
]