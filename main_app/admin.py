from django.contrib import admin
# import your models here
from .models import Rep, Category

# Register your models here
admin.site.register(Rep)
admin.site.register(Category)